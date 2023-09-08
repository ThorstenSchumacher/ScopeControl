####################################################################################################################################################
# ScopeControl
# by Thorsten Schumacher - PrintedLabs
#
# Licence: Creative Commons Attribution-NonCommercial-ShareAlike (CC BY-NC-SA) 
# also see: https://creativecommons.org/licenses/by-nc-sa/4.0/deed.de
#
# A slim uvc camera viewer with basic camera control functions, some live view filter functions and tools for microscopic and astronomical measurements, 
# image averaging and a simple timelapse tool. It also includes the software interface to our 3D-printed microscope, telescope and telescope mount.
###################################################################################################################################################


# import relevant external modules
# import required packages
import cv2     # openCV for live view
import numpy as np   # numpy for data processing
import sys  # general lib
import time # general lib
import nest_asyncio # get rid of async warnings (event loop issue)
import csv  # read config data and micobjective List
import serial, serial.tools.list_ports  # communicate with microscope (lamp)
from os import getcwd as getfolder
from os import makedirs
from os.path import exists as fileexists
from os.path import isdir as isdir
import pygetwindow as gw # to get window position and size for recreation


# UI 
from threading import Thread
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog
import PySide6.QtCore as qtc
from PySide6.QtGui import QIcon

# import own modules and gui
from interface_cam.camcom_gui import Ui_camcom_mainwin
from interface_cam.Workerclass import CamreadWorker, Lampconnect, Camconnect
nest_asyncio.apply() 


################## class for status messages #####################
class Statusemitter(qtc.QObject):
    messagesignal = qtc.Signal(str)

    def sendmessage(self, mymessage)    :
        self.messagesignal.emit(mymessage)

##############################################################################################################################################
#                                                          MAIN WINDOW
##############################################################################################################################################

class camwin(QMainWindow):
    
     ## initializing stuff when class is called ... all for/inside GUI
    def __init__(self, interfacenum, parentwin, *args, **kwargs):

        super().__init__(*args, **kwargs)
        # stuff for window
        self.ui =  Ui_camcom_mainwin()
        self.ui.setupUi(self)
        self.interfacennr = interfacenum
        self.setWindowFlags(self.windowFlags() | qtc.Qt.WindowStaysOnTopHint) #keep control panel on top
        self.setWindowFlag(qtc.Qt.FramelessWindowHint) ## we dont want to see the window frame
        self.setAttribute(qtc.Qt.WA_TranslucentBackground) ## we dont want to see the window frame
        self.ui.label_status.setStyleSheet("color:#ff0000; background-color: transparent; border-color: transparent; font-size: 12pt") ## to keep the format
        self.ui.label.setStyleSheet("color: rgb(240,240,240); font-weight: bold; background-color: transparent; border-color: transparent; font-size: 14pt") ## to keep the format
        self.parentwin = parentwin # here we have the parent window (experimental control)
        self.windowsizeY = [360, 526, 756, 596] # this are the two window sizes the small one without settings, the big one with settings
        self.frame4pos = [295, 460] # this is where we want to have the image manipulation menu
        self.menu2pos = [350, 510]
        self.ui.frame.setFixedHeight(self.windowsizeY[0]) # this is the frame with content
        self.setFixedHeight(self.windowsizeY[0]) # this is the outer window frame
        self.ui.lineEdit_filepath.setText(getfolder()) # preset current directory
        self.checksavefolder(0) # we check if the savefolder exists and if not, we create it = 0 ... if = 1 we also create the datefolder (if we press any button)
        self.windowRestored = qtc.Signal() # we need this one if the window is restored after minimizing
        self.setWindowIcon(QIcon('confs/SWicon.png'))  # use this icon on the OS
        self.setWindowTitle("ScopeControl - PrintedLabs")  # this is the Frame Title (shown as WindowName in OS)
        self.ui.label_36.setOpenExternalLinks(True) # this allows the click the link in the infobox ... label36
        self.ui.pushButton_comconnect.setDisabled(True) # dont push the button before cameras are scanned .. will be enabled by camscanner
        self.ui.pushButton_comrefresh.setDisabled(True) # dont push the button before cameras are scanned .. will be enabled by camscanner
        # to give the SW an Icon (e.g. TaskManager ...) use in pyintaller ....  "pyinstaller --onefile --noconsole --icon=confs/SWicon.png ScopeControl.py"
        self.ui.stackedWidget_scopetype.setVisible(False)
        self.ui.frame_4.setGeometry(self.ui.frame_3.x(), self.frame4pos[0], self.ui.frame_3.width(), self.ui.frame_3.height())

        # prepare statusmessage signal - connection 
        self.messageemitter = Statusemitter()           # create an Object for signal emission containing the signal send function
        self.messageemitter.messagesignal.connect(self.statusmessage) # this will be the target function of our signal
        self.move(self.parentwin.intwinpos[0], self.parentwin.intwinpos[1]) # move the window to its position
        self.parentwin.intwinpos[1] += 286  #   store in parent window the position for the next interface window
        self.show()

        # start update thread
        self.threadpool = qtc.QThreadPool()
        
        # define flags
        self.runcam = False # initialy the cam is not running
        self.videomin = False # we will not start in minimized video window
        self.fullscreenmode = True # if true, there is no window frame but the whole sceen will be the live-view, if false we have the live-view windowed
        self.recreatewin = True # we start the window for the first time
        self.freeze = False # if true we will skip grabbing a ned frame
        self.vidrec = False # flag if we are recording a video
        self.settingsopen = False # flag if settings are open
        self.averagemode = False # flag if we want to average over frames
        self.micmode = False # we are in microscope mode
        self.telmode = False # we are in telescope mode
        self.infomode = False # we show the infobox
        self.imageparaopen = False # we have the image processing box open
        self.menu1open = False # iw we show the scope stacked widget
        self.menu2open = False # if we show the lower stacked widget
        self.measurescale = 0 # it is more easy to have a scale ID 0 = pixel, 1 = µm from microscope , 2 = opening angle (telescope)  .. we start with pixel measurements
        self.avID = 0 # average frame ID (runs from 0 to average limit)


        # available sources (IDs) for cv2 and other camera parameters
        self.camindexfound = ["0"] #we start with one source
        self.ui.comboBox_camport.addItems(self.camindexfound)
        self.frameid = 0    # the frame number we got after connecting to the cam
        self.resolutiondesired = [2*1920, 2*1080] # this is the desired resolution we are working with ... 
        self.resolution = [2*1920, 2*1080] # self.resolution will be overwritten when cam is connected and readout
        self.averagenum = 20 # over how many frames we want to average
        self.vidtime0 = 0 # this is the time when we will start recording
        self.vidtime1 = 0 # this is the time when the last frme was written
        self.TLperiode = float(1.0) # seconds we write until we write a new frame to video file
        self.screenpos = [0, 0] # here we place the live view window (for the first time)
        self.screenwin = self.resolution # will be overwritten with the real cam resolution and also overwritten if we resize the non fullscreen window ... for recreation
        

        # image processing params
        self.lightness = self.saturation = 1 # value for lightness and saturation
        self.contrast = 2   # for HDR
        self.contrast2 = 8  # for HDR

        # empty frame
        self.frameid = 0    # the frame number we got after connecting to the cam
        self.framesave = np.zeros([self.resolution[1], self.resolution[0], 3], dtype=np.uint8)  # zero frame .. will be updated when cam is connected frame is without information on top, framesave is with info and this is the frame that will be stored
        
        ## positions/ cursor
        self.measuring = False    # flag if we are in the two-point measuring routine
        self.measureID = 0 # to know the step of our measurement
        self.campxsize = 2.8 # start value for pixel length of camera
        self.ui.lineEdit_pxlen.setText(str(self.campxsize))
        self.cursorxlive = self.cursorx0 = self.cursorx1 = 0  # all the x and y coordinates we need to store
        self.cursorylive = self.cursory0 = self.cursory1 = 0 

        ## setup mount and telescope control
        self.telID = 0 # we
        self.mountstepsize = 3 # stepsize / speed of mount when pushing arrow buttons
        self.setmountstepsize() # read current value

        ## microscope setup calibration and stuff
        self.objID = 0
        self.setexposuretime() # to update slider and labels
        self.setbrightness() # to update slider and labels
        self.setgain() # ... what is now the averager ... to update slider and labels
        self.getdatabase() # get all the objectives that we have in our database file "objectives.csv"
        self.ui.horizontalSlider_lightness.setValue(12) # set current lightness value to 1
        self.setlightness() # set lightness to initial value
        self.setsaturation() # set lightness to initial value
        self.setcontrast() # set lightness to initial value
        

        ## setup lamp connection
        self.portscan() # ... get com ports
        self.illumodes = ["Illumination - off","Brightfield - white light", "Darkfield - white light", "Darkfield - red light", "Darkfield - green light", "Darkfield - blue light"]
        self.ui.comboBox_illumode.addItems(self.illumodes)
        self.ui.comboBox_illumode.setDisabled(True)
        self.ui.horizontalSlider_lampinten.setDisabled(True)

       

        ## finally we load the saved settings if available
        self.ui.horizontalSlider_exposure.setRange(-13, 0)
        self.scancam()
        self.loadsettings()

    ########################################## UI buttons ####################################################
        
        # general stuff
        self.ui.pushButton_comrefresh.clicked.connect(self.scancam)
        self.ui.pushButton_comconnect.clicked.connect(self.launchcamconnect)
        self.ui.pushButton_lamprefresh.clicked.connect(self.portscan)
        self.ui.pushButton_mountrefresh.clicked.connect(self.portscan)
        self.ui.pushButton_lampconnect.clicked.connect(self.launchcomconnect)
        self.ui.pushButton_settings.clicked.connect(self.opensettings)
        self.ui.pushButton_exit.clicked.connect(self.closeSW)
        self.ui.pushButton_mini.clicked.connect(self.minimize)
        self.ui.pushButton_screenmode.clicked.connect(self.fullscreentoggle)
        self.ui.pushButton_micmode.clicked.connect(self.gotomicmode)
        self.ui.pushButton_telmode.clicked.connect(self.gototelmode)
        self.ui.pushButton_infobox.clicked.connect(self.gotoinfomode)

        #camcontrol
        self.ui.horizontalSlider_exposure.valueChanged.connect(self.setexposuretime)
        self.ui.horizontalSlider_bright.valueChanged.connect(self.setbrightness)
        self.ui.horizontalSlider_gain.valueChanged.connect(self.setgain)
        self.ui.pushButton_freeze.clicked.connect(self.togglefreeeze)
        self.ui.pushButton_record.clicked.connect(self.recordvid)
        self.ui.pushButton_average.clicked.connect(self.averager)
        self.ui.pushButton_imagepara.clicked.connect(self.imagepara)
        self.ui.lineEdit_frameavnum.textChanged.connect(self.checkframeaveragenumber)
        self.ui.lineEdit_Ttimelaps.textChanged.connect(self.checkTperiod)


        # image processing
        self.ui.horizontalSlider_lightness.valueChanged.connect(self.setlightness)
        self.ui.horizontalSlider_saturation.valueChanged.connect(self.setsaturation)
        self.ui.horizontalSlider_contrastamp.valueChanged.connect(self.setcontrast)
        self.ui.horizontalSlider_contrastgrid.valueChanged.connect(self.setcontrast)
        

        # lampcontrol
        self.ui.comboBox_illumode.currentTextChanged.connect(self.setillumode)
        self.ui.horizontalSlider_lampinten.valueChanged.connect(self.setilluintens)

        # mountcontrol
        self.ui.pushButton_mountconnect.clicked.connect(self.mountconnect)
        self.ui.horizontalSlider_mountspeed.valueChanged.connect(self.setmountstepsize)

        #save buttons 
        self.ui.pushButton_saveimg.clicked.connect(self.clicksaveimg)
        self.ui.pushButton_browse.clicked.connect(self.browsefiles)
        
        #measure and scope settings
        self.ui.pushButton_measure.clicked.connect(self.measure)
        self.ui.comboBox_micobject.currentTextChanged.connect(self.objselect)
        self.ui.comboBox_telescopes.currentTextChanged.connect(self.telselect)

        # save/load settings
        self.ui.pushButton_savesettings.clicked.connect(self.writesettings)
        self.ui.pushButton_loadsettings.clicked.connect(self.loadsettings)

    ####################################### move frameless window ############################################
    
    def mousePressEvent(self, event):
        p = event.globalPosition()
        globalPos = p.toPoint()
        self.oldPos = globalPos

    def mouseMoveEvent(self, event):
        p = event.globalPosition()
        globalPos = p.toPoint()
        delta = qtc.QPoint(globalPos - self.oldPos) 
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = globalPos

    ###################################### general functions ##################################################
    def fullscreentoggle(self):
        self.keepwindowpos()
        self.videomin = True
        self.fullscreenmode = not(self.fullscreenmode) # we toggle the current fullscreenmode
        time.sleep(0.05)
        self.videomin = False
        self.recreatewin = True # and recreate the window
    
    def minimize(self):
        self.keepwindowpos() # stores the live view window properties (position and size)
        self.showMinimized() # minimize control panel
        self.videomin = True # minimize video window

    def keepwindowpos(self):
        if cv2.getWindowProperty("live-view", cv2.WND_PROP_VISIBLE) != 0 and not(self.fullscreenmode): # if there is a live screen, then we keep its last position
            x, y, width, height = cv2.getWindowImageRect('live-view')
            self.screenwin = [width, height]
            self.screenpos = [x-8, y-31] # here we place the live view window after recreation

    def writesettings(self):
        configarray = [self.ui.comboBox_camport.currentIndex(), self.ui.comboBox_lampport.currentIndex(), self.ui.comboBox_micobject.currentIndex(), self.ui.lineEdit_pxlen.text(), self.ui.lineEdit_frameavnum.text(), self.ui.comboBox_mountport.currentIndex(), self.ui.comboBox_telescopes.currentIndex()]  # create list with all information to save
        np.save("confs/config.npy", configarray) # write config file
        self.messageemitter.sendmessage("settings saved") # and send statusmessage

    def loadsettings(self):
        if fileexists("confs/config.npy"):
            configarray = np.load("confs/config.npy")     # load file
            # now restore all the settings
            self.ui.comboBox_camport.setCurrentIndex(int(configarray[0]))
            self.ui.comboBox_lampport.setCurrentIndex(int(configarray[1]))
            self.ui.comboBox_micobject.setCurrentIndex(int(configarray[2]))
            self.ui.lineEdit_pxlen.setText(str(configarray[3]))
            self.ui.lineEdit_frameavnum.setText(str(configarray[4]))
            self.ui.comboBox_mountport.setCurrentIndex(int(configarray[5]))
            self.ui.comboBox_telescopes.setCurrentIndex(int(configarray[6]))
            self.objselect() # and execute the object selection ... so that our objID is up2date
            self.telselect() # and the same for the telescopes
            self.messageemitter.sendmessage("config file loaded") # send message
        else:
            self.messageemitter.sendmessage("") # or if no config file was found ... reset statuslabel

    def checksavefolder(self, mode):
  
        if mode == 0: # we generate the savedata folder if necessary
            pathname1 = self.ui.lineEdit_filepath.text() + "\savedata" # first we check if savedata folder exists
            if fileexists(pathname1) and isdir(pathname1):
                pass
            else:
                makedirs(pathname1)
            self.ui.lineEdit_filepath.setText(pathname1)
   
         
        if mode == 1: # now we check if the date path also exists
            pathname1 = self.ui.lineEdit_filepath.text() # first we check if savedata folder exists
            
            if fileexists(pathname1) and isdir(pathname1):
                return True
            else:
                return False

    def statusmessage(self, text):          # writes a message to the status label and resets it after 3000ms
        self.ui.label_status.setText(text)  # the message is set
        qtc.QTimer.singleShot(3000, self.resetstatus)   #after 3000ms we call the resetstatus function that writes "waiting" again

    def resetstatus(self):  # resets the status label to waiting
        self.ui.label_status.setText("")
    
    def closeSW(self):
        # CAM
        self.runcam = False         # set flag to interrupt frame grabbing       
        try:
            self.mycam.release()    # try to close the cam connection (if no cam is connected its also fine)
        except:
            pass
        # LAMP
        try:                        # try disconnecting lamp
            if self.ui.pushButton_lampconnect.text() == "disconnect":            
                self.closecom()
        except:
            pass
        
        #UI
        self.close()                # close UI




    def changeEvent(self, event):    # changeevent for window is overwritten (is called whenever the Windowstate has changed)
        if event.type() == event.WindowStateChange and self.videomin == True:
            # we set the flags to create the cv2 window and plot the live-images again
            self.recreatewin = True # Flag: create a new CV2 window 
            self.videomin = False # Flag: minimize video window
        super().changeEvent(event)


    def opensettings(self):         # toggles between settings window is shown or not
        if self.imageparaopen == True:
            self.imagepara()     #   if the image parameter menu is open, simply turn it off

        if self.settingsopen == False: 
            self.ui.pushButton_settings.setStyleSheet(u""+ self.buttonstyle("settings.png", "settingsb.png", 1)) # set to activated mode
            self.ui.stackedWidget_settings.setCurrentIndex(0)
            self.settingsopen = True
            
        else:
            self.ui.pushButton_settings.setStyleSheet(u""+ self.buttonstyle("settings.png", "settingsb.png", 0)) # set to unactivated mode
            self.settingsopen = False
        
        self.menusetup()

    def objselect(self):
        self.objID = self.ui.comboBox_micobject.currentIndex()

    def buttonstyle(self, image, imagehover, pressmode): # image is the image button of the style, pressmode: 0 = set to unactivated, 1 = set to activated mode
        if pressmode == 1:
            stylecode = "QPushButton {\n border: none;\n border-radius: 0px;\n	background-color: rgb(100, 150, 200);\n	background-image: url(:/icons/"+ image +");\n	color: white;\n}\n \n QPushButton:hover {\n	background-image: url(:/icons/"+ imagehover +");\n	color: white;\n}\n \n QPushButton:pressed {\n background-color: rgb(130, 180, 230);\n color: white;\n}"
        if pressmode == 0:
            stylecode = "QPushButton {\n border: none;\n border-radius: 0px;\n	background-color: rgb(90, 90, 90);\n	background-image: url(:/icons/"+ image +");\n	color: white;\n}\n \n QPushButton:hover {\n	background-image: url(:/icons/"+ imagehover +");\n	color: white;\n}\n \n QPushButton:pressed {\n background-color: rgb(130, 180, 230);\n color: white;\n}"
        return stylecode
    
    def buttonstylenoImage(self, pressmode): # image is the image button of the style, pressmode: 0 = set to unactivated, 1 = set to activated mode
        if pressmode == 1:
            stylecode = "QPushButton {\n border: none;\n border-radius: 0px;\n  font: 75 10pt \"MS Shell Dlg 2\";\n background-color: rgb(100, 150, 200);\n	color: rgb(220, 220, 220);\n}\n \n QPushButton:hover {\n	color: white;\n}\n \n QPushButton:pressed {\n background-color: rgb(130, 180, 230);\n color: white;\n}"
        if pressmode == 0:
            stylecode = "QPushButton {\n border: none;\n border-radius: 0px;\n	font: 75 10pt \"MS Shell Dlg 2\";\n background-color: rgb(90, 90, 90);\n color: rgb(220, 220, 220);\n}\n \n QPushButton:hover {\n color: white;\n}\n \n QPushButton:pressed {\n background-color: rgb(130, 180, 230);\n color: white;\n}"
        return stylecode
    
    def buttonstyleREC(self, image, imagehover, pressmode): # image is the image button of the style, pressmode: 0 = set to unactivated, 1 = set to activated mode
        if pressmode == 1:
            stylecode = "QPushButton {\n border: none;\n border-radius: 0px;\n	background-color: rgb(180, 0, 0);\n	background-image: url(:/icons/"+ image +");\n	color: white;\n}\n \n QPushButton:hover {\n	background-image: url(:/icons/"+ imagehover +");\n	color: white;\n}\n \n QPushButton:pressed {\n background-color: rgb(255, 0, 0);\n color: white;\n}"
        if pressmode == 0:
            stylecode = "QPushButton {\n border: none;\n border-radius: 0px;\n	background-color: rgb(90, 90, 90);\n	background-image: url(:/icons/"+ image +");\n	color: white;\n}\n \n QPushButton:hover {\n	background-image: url(:/icons/"+ imagehover +");\n	color: white;\n background-color: rgb(155, 0, 0);\n}\n \n QPushButton:pressed {\n background-color: rgb(255, 0, 0);\n color: white;\n}"
        return stylecode
    

    
    def gotomicmode(self): 
        if self.micmode == False:        
            self.setmodestofalse() # set all modes to False (in case we add some more)
            self.measurescale = 1 # we use the microscope data for measurements in the image
            self.ui.stackedWidget_scopetype.setCurrentIndex(0)
            self.micmode = True
            self.ui.pushButton_micmode.setStyleSheet(u""+ self.buttonstylenoImage(1)) # set to activated mode (button)
            self.menusetup()
        else:
            self.setmodestofalse() # set all modes to False (in case we add some more)
            self.menusetup()


    def gototelmode(self):
        if self.telmode == False:
            self.setmodestofalse() # set all modes to False (in case we add some more)
            self.measurescale = 2 # we use the telescope data for measurements in the image
            self.ui.stackedWidget_scopetype.setCurrentIndex(1)
            self.telmode = True
            self.ui.pushButton_telmode.setStyleSheet(u""+ self.buttonstylenoImage(1)) # set to activated mode (button)
            self.menusetup()
        else:
            self.setmodestofalse() # set all modes to False (in case we add some more)
            self.menusetup()

    def gotoinfomode(self):
        if self.infomode == False:
            self.setmodestofalse() # set all modes to False (in case we add some more)
            self.ui.stackedWidget_scopetype.setCurrentIndex(2)
            self.infomode = True
            self.ui.pushButton_infobox.setStyleSheet(u""+ self.buttonstyle("info.png", "infob.png", 1)) # set to activated mode
            self.menusetup()
        else:
            self.setmodestofalse() # set all modes to False (in case we add some more)
            self.menusetup() 

    def setmodestofalse(self):
        self.measurescale = 0 # here we reset the scale ID for the measurement option ... if 
        self.micmode = False
        self.telmode = False
        self.infomode = False
        self.ui.pushButton_micmode.setStyleSheet(u""+ self.buttonstylenoImage(0)) # set to unactivated mode (button)
        self.ui.pushButton_telmode.setStyleSheet(u""+ self.buttonstylenoImage(0)) # set to unactivated mode (button)
        self.ui.pushButton_infobox.setStyleSheet(u""+ self.buttonstyle("info.png", "infob.png", 0)) # set to unactivated mode
        
    def menusetup(self):
        if any([self.micmode, self.telmode, self.infomode]):
                self.ui.stackedWidget_scopetype.setVisible(True)
                self.ui.frame_4.setGeometry(self.ui.frame_4.x(), self.frame4pos[1], self.ui.frame_3.width(), self.ui.frame_3.height())
                self.ui.stackedWidget_settings.setGeometry(self.ui.stackedWidget_settings.x(), self.menu2pos[1], self.ui.stackedWidget_settings.width(), self.ui.stackedWidget_settings.height())
                if any([self.settingsopen, self.imageparaopen]):
                    self.ui.frame.setFixedHeight(self.windowsizeY[2]) # this is the frame with content
                    self.setFixedHeight(self.windowsizeY[2])
                else:
                    self.ui.frame.setFixedHeight(self.windowsizeY[1]) # this is the frame with content
                    self.setFixedHeight(self.windowsizeY[1])
        else:
            self.ui.stackedWidget_scopetype.setVisible(False)
            self.ui.frame_4.setGeometry(self.ui.frame_4.x(), self.frame4pos[0], self.ui.frame_3.width(), self.ui.frame_3.height())
            self.ui.stackedWidget_settings.setGeometry(self.ui.stackedWidget_settings.x(), self.menu2pos[0], self.ui.stackedWidget_settings.width(), self.ui.stackedWidget_settings.height())
            if any([self.settingsopen, self.imageparaopen]):
                self.ui.frame.setFixedHeight(self.windowsizeY[3]) # this is the frame with content
                self.setFixedHeight(self.windowsizeY[3])
            else:
                self.ui.frame.setFixedHeight(self.windowsizeY[0]) # this is the frame with content
                self.setFixedHeight(self.windowsizeY[0])
    
    ####################################### microscope/lamp connection and functions ##########################################

    def portscan(self):
        myports = [tuple(p) for p in list(serial.tools.list_ports.comports())]        
        usb_port_list = [p[0] for p in myports]
        self.ui.comboBox_lampport.clear()
        self.ui.comboBox_lampport.addItems(usb_port_list)
        self.ui.comboBox_mountport.clear()
        self.ui.comboBox_mountport.addItems(usb_port_list)

    def launchcomconnect(self):
        if self.ui.pushButton_lampconnect.text() == "disconnect":
            self.closecom()
            self.ui.pushButton_lampconnect.setText("connect")
            self.ui.comboBox_illumode.setDisabled(True)
            self.ui.horizontalSlider_lampinten.setDisabled(True)
            self.ui.pushButton_lampconnect.setEnabled(True)
            self.ui.pushButton_lamprefresh.setEnabled(True)
        else:
            self.messageemitter.sendmessage("connecting to lamp")
            self.ui.pushButton_lampconnect.setDisabled(True)
            self.ui.pushButton_lamprefresh.setDisabled(True)
            self.comlaunchworker = Lampconnect(self)
            self.threadpool.start(self.comlaunchworker)

    def connect2com(self): ## connect to arduino    

        try:
            self.ser = serial.Serial(port=str(self.ui.comboBox_lampport.currentText()), baudrate=115200, timeout = 3)
            time.sleep(2)
            serialcommand = "ard.areyouamicroscope\n"
            self.ser.write(serialcommand.encode())   # ask if arduino is online                
            time.sleep(0.15)
            response = self.ser.readline().decode("utf-8")
            time.sleep(0.15)
            if self.ser.isOpen() == True and response == "ard.lamponline;\r\n":    # connection works and device identified as microscope
                self.ui.pushButton_lampconnect.setText("disconnect")
                self.ui.comboBox_illumode.setCurrentIndex(1) # finally we set the standard illumination to bright field (with full intensity)
                self.ui.comboBox_illumode.setEnabled(True)
                self.ui.horizontalSlider_lampinten.setEnabled(True)
                self.messageemitter.sendmessage("lamp connected")
            else:   # otherwise disconnect and reset ui
                self.ui.pushButton_lamprefresh.setEnabled(True)
                self.ui.comboBox_illumode.setDisabled(True)
                self.ui.horizontalSlider_lampinten.setDisabled(True)
                self.ser.close()
                self.messageemitter.sendmessage("lamp connection failed")
        except:
            pass
        self.ui.pushButton_lampconnect.setEnabled(True)

    def closecom(self):  #close communication
        time.sleep(0.2) # to be shure that the updateloop was at the interrupt event
        try:
            serialcommand = "ard.mode0\n"   # we send the illumination 0 = everything off command
            self.ser.write(serialcommand.encode())   # ask if arduino is online 
            time.sleep(0.5)
            self.ui.comboBox_illumode.setCurrentIndex(0) # thsi automatically will send illumode signal to 0
            self.ui.pushButton_lampconnect.setText("connect")   # change button text
            self.messageemitter.sendmessage("lamp disconnected")
            del(self.ser) # finally we delete the whole object
            self.ui.comboBox_illumode.setDisabled(True)
            self.ui.horizontalSlider_lampinten.setDisabled(True)
            time.sleep(0.25)
            self.ser.close() # afterwards close serial connection
        except:
            pass

    def setillumode(self):
        serialcommand = "ard.mode"+str(self.ui.comboBox_illumode.currentIndex())+"\n"
        self.ser.write(serialcommand.encode())   # send command

    def setilluintens(self):
        self.ui.label_bright_2.setText(str(self.ui.horizontalSlider_lampinten.value()))
        val = int(2.55*self.ui.horizontalSlider_lampinten.value()) # we generate the 8 bit illumination intensity 0 ... 254
        serialcommand = "ard.lampintens"+str(val)+"\n"   # prepare command
        self.ser.write(serialcommand.encode())   # send command 


    ####################################### telescope/mount connection and functions ##########################################

    def mountconnect(self):
        self.statusmessage("not yet implemented")

    def setmountstepsize(self):
        self.mountstepsize = self.ui.horizontalSlider_mountspeed.value()
        self.ui.label_mountspeed.setText(str(self.mountstepsize))

    def telselect(self):
        self.telID = self.ui.comboBox_telescopes.currentIndex()

    ###################################### camera readout and interface #########################################

    def returnCameraIndexes(self): # this function searches the first "ports" for an camera and stores the found ids
        
        # checks the first 10 indexes.
        index = 0
        camindexfound = []

        while True:
            cap = cv2.VideoCapture(index, cv2.CAP_DSHOW)  # Use cv2.CAP_DSHOW for Windows

            if not cap.isOpened(): # we are done if no furter camera is found
                break

            _, frame = cap.read()  # Read a frame to check if the camera is working

            if frame is not None: # we find out if there is a frame
                camindexfound.append(str(index)) # the we add the camera as camera
            
            cap.release() # release the cam
            index += 1 # and go to next index

        # finally we update the combobox and store the result in the object
        self.ui.comboBox_camport.clear()    
        self.ui.comboBox_camport.addItems(camindexfound)  
        self.camindexfound = camindexfound
        self.ui.comboBox_camport.setEnabled(True) # we disable the combobox so that nobody can press it while scanning
        self.ui.pushButton_comconnect.setEnabled(True) # enable connect and refresh buttons again
        self.ui.pushButton_comrefresh.setEnabled(True) # enable connect and refresh buttons again

        self.resetstatus() # we are done scanning what propably takes longer than 3 seconds


    def scancam(self):  # we start scanning available camera sources within a thread .. so that nothing freezes
        # scanning can take a long time .. so we keep the status on "scanning"
        self.ui.comboBox_camport.setDisabled(True) # we disable the combobox so that nobody can press it while scanning
        self.ui.pushButton_comconnect.setDisabled(True) # dont push the button before cameras are scanned .. will be enabled after scan again
        self.ui.pushButton_comrefresh.setDisabled(True) # dont push the button before cameras are scanned .. will be enabled after scan again
        self.ui.label_status.setText("scanning camera sources") # set text to scanning
        self.ui.label_status.repaint()
        # we start a thread doing the work and scanning
        scanthread = Thread(target = self.returnCameraIndexes, args=()) 
        scanthread.start()

    def launchcamconnect(self):
        if self.vidrec: # if recording we are in connected mode and at to disconnect ... so we imediately interrupt the movie before disconnectiong hardware
            self.recordvid()

        # if there is a camera in the list
        if self.ui.comboBox_camport.currentIndex() >= 0:
            self.camlaunchworker = Camconnect(self)
            self.threadpool.start(self.camlaunchworker)
        else:
            self.statusmessage("no camera port")

    def connect2cam(self):
        if self.ui.pushButton_comconnect.text() == "connect": # in case we are not connected but want to
            self.ui.pushButton_comconnect.setDisabled(True) # set buttons and menu disabled to avoid starting a second process
            self.ui.pushButton_comrefresh.setDisabled(True)
            self.ui.comboBox_camport.setDisabled(True)
            self.messageemitter.sendmessage("connecting to camera")
            
            # open camera
            self.mycam = cv2.VideoCapture(int(self.ui.comboBox_camport.currentText()), cv2.CAP_DSHOW)  # , cv2.CAP_MSMF is suggested backend but also default, cv2.CAP_DSHOW comes from chatGPT
           
            # now set camera parameters
            self.ui.pushButton_comconnect.setText("disconnect")
            if self.mycam.isOpened():
                self.mycam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
                self.mycam.set(cv2.CAP_PROP_FRAME_WIDTH, self.resolutiondesired[0])
                self.mycam.set(cv2.CAP_PROP_FRAME_HEIGHT, self.resolutiondesired[1])
                self.mycam.set(cv2.CAP_PROP_AUTO_WB, 0.75) # thies deactivates white balance
                self.mycam.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.25) # deactivates auto exposure
                self.mycam.set(cv2.CAP_PROP_FPS, 30)

                #  since we can only wish a resultion but that depends on the hardware lets see what we got and store it
                self.resolution[1] = int(self.mycam.get(cv2.CAP_PROP_FRAME_HEIGHT))
                self.resolution[0] = int(self.mycam.get(cv2.CAP_PROP_FRAME_WIDTH))
                self.screenwin = self.resolution # after a new camera connection we always start with a live with with full size

                # now we set the camera parameter for the first time
                self.runcam = True  # we set the flag! and afterwards we update the set cam parameter
                self.setexposuretime() # to update slider and labels
                self.setbrightness() # to update slider and labels
                self.setgain() # ... what is now the averager ... to update slider and labels
           
                # now start reading the cam in a separate thread
                self.camreadworker = CamreadWorker(self)
                self.ui.pushButton_comconnect.setEnabled(True)
                self.threadpool.start(self.camreadworker)   # run camera thread
                self.messageemitter.sendmessage("camera connected") # and send status
                
            
            else:
                self.messageemitter.sendmessage('failed')
                # and set all buttons enabled
                self.ui.pushButton_comconnect.setEnabled(True)
                self.ui.pushButton_comrefresh.setEnabled(True)
                self.ui.comboBox_camport.setEnabled(True)
                self.ui.pushButton_comconnect.setText("connect")

        
        else: # in case we want to disconnect
            self.runcam = False # stop loop 
            time.sleep(0.25) # and give it some time before we release the camera
            
            # reset UI buttons      
            self.ui.pushButton_comconnect.setText("connect")
            self.ui.pushButton_comconnect.setEnabled(True)
            self.ui.pushButton_comrefresh.setEnabled(True)
            self.ui.comboBox_camport.setEnabled(True)
            self.messageemitter.sendmessage("disconnected from camera")
            
            # release camera after everything else is done
            self.mycam.release()

    
    def camreadupdate(self):
        self.frameid = 0    # after connecting to cam we start with frame nr 0  


        # now we start reading
        while self.runcam == True:
            if self.recreatewin == True:    # we have to define our window since the camera starts for the first time or we come back from minimized window
                # we prepare the window for full frame image ... to adjust
                cv2.namedWindow('live-view', cv2.WINDOW_NORMAL)
                cv2.resizeWindow('live-view', self.screenwin[0], self.screenwin[1])
                cv2.moveWindow('live-view', self.screenpos[0], self.screenpos[1])
                if self.fullscreenmode == True:   # if we have fullscreenmode activated, we will have the whole screen as live-view
                    cv2.setWindowProperty('live-view', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

                self.recreatewin = False   # after creation we no longer need to do that

                # we get one single frame when creating the window ... afterwards it can directly pause
                self.rval, frame = self.mycam.read() 
                framelive = freezeframe = self.imagemani(frame)
            
            
            # grab new frame
            if self.freeze == False: # we only grab a new frame if we are not in freeze mode
                self.rval, frame = self.mycam.read() 
                freezeframe = frame

                # averager mode
                if self.averagemode == True:
                    if self.avID == 0:  # we start the averaging with empty lists and data
                        framebuffer = [] # start framebuffer list
                        sumframe = sumframecorr = np.uint16(0*frame) # initial "empty" frame with 16 bit (to add up several frames with 8 bit depht)
                            
                    if self.avID > self.averagenum - 1: # the buffer is full and we compute some kind of moving average
                                             
                        sumframecorr = np.subtract(sumframe, framebuffer[0])  # we use numpy operation to work in float64bit and avoid
                        framebuffer.pop(0) # remove the oldest frame
                        framebuffer.append(np.uint16(frame)) # add the latest frame to the list (its just for subtracting the average frame)
                        sumframe = np.add(sumframecorr , framebuffer[-1]) # now we add the last frame to the sum ... the average is build in uint8 convertion for frame

                    else: #  if we have not jet reached the full framseset to avera
                        framebuffer.append(frame) # add the frame to the frambuffer (for later subtraction)
                        sumframe = cv2.addWeighted(sumframe, 1, np.uint16(frame), 1, 0) # we save everthying
                       
                    self.avID += 1 # this is an endless fram counter that counts from the beginning of the average mode

                    # now we save the averaged frame to the current frame and handle it as usual in liveview
                    frame = freezeframe = np.uint8(sumframe/len(framebuffer)) # in case of freeze mode we want to show the averaged frame
                    
                    # check if the buffer is filled up for the first time then we autostop
                    if self.avID == self.averagenum: # we autostop the averaging ... but 
                        self.togglefreeeze()
                        self.statusmessage("autostop - averaged")
                

            else: # or keep the old one and overwrite it with the stored one (without data and lines etc.)
                frame = freezeframe


            # flip x - y function
            framelive = self.imagemani(frame)

            # liveview BW
            if self.ui.checkBox_grayscale.isChecked() == True:  # if it is checked we overwrite the liveframe with its BW version
                frame = cv2.cvtColor(framelive, cv2.COLOR_BGR2GRAY) # in grayscale
            else: 
                frame = framelive # or keep it in color
            
            self.frameid += 1 # we give it the current frame ID
            frmSat = np.amax(frame) # for saturation alarm
       
            if self.ui.checkBox_imginfo.isChecked() == True:    # if we want to see the additional infos
                
                if frmSat >= 240:
                    frame = cv2.putText(
                    frame,
                    text = "Saturation: > 95 % warning!!!",
                    org = (30, 60),
                    fontFace = cv2.FONT_HERSHEY_DUPLEX,
                    fontScale = 1.0,
                    color = (0, 0, 0.6*255),
                    thickness = 1
                    )
                else:
                    frame = cv2.putText(
                    frame,
                    text = "Saturation: "+"{:.2f}".format(100*frmSat/255)+" %",
                    org = (30, 60),
                    fontFace = cv2.FONT_HERSHEY_DUPLEX,
                    fontScale = 1.0,
                    color = (0, 0, 0.6*255),
                    thickness = 1
                    )
        
                # show integration time
                frame = cv2.putText(
                frame,
                text = "Max. FPS: {:.2f}".format(self.mycam.get(cv2.CAP_PROP_FPS)),
                org = (30, 30),
                fontFace = cv2.FONT_HERSHEY_DUPLEX,
                fontScale = 1.0,
                color = (0, 0, 0.6*255),
                thickness = 1
                )

                # show camera parameter
                frame = cv2.putText(
                frame,
                text = "Exposure val: {:.1f}".format(-1*self.ui.horizontalSlider_exposure.value()),
                org = (30, 90),
                fontFace = cv2.FONT_HERSHEY_DUPLEX,
                fontScale = 1.0,
                color = (0, 0, 0.6*255),
                thickness = 1
                )

                frame = cv2.putText(
                frame,
                text = "Brightness: {:.1f} %".format(self.ui.horizontalSlider_bright.value()),
                org = (30, 120),
                fontFace = cv2.FONT_HERSHEY_DUPLEX,
                fontScale = 1.0,
                color = (0, 0, 0.6*255),
                thickness = 1
                )

                frame = cv2.putText(
                frame,
                text = "Gain: {:.1f}".format(self.ui.horizontalSlider_gain.value()),
                org = (30, 150),
                fontFace = cv2.FONT_HERSHEY_DUPLEX,
                fontScale = 1.0,
                color = (0, 0, 0.6*255),
                thickness = 1
                )

                frame = cv2.putText(
                    frame,
                    text = "cursor-coordinates: x={:.0f}".format(self.cursorxlive) + " y=" + "{:.0f}".format(self.cursorylive),
                    org = (30, 180),
                    fontFace = cv2.FONT_HERSHEY_DUPLEX,
                    fontScale = 1.0,
                    color = (0, 0, 0.6*255),
                    thickness = 1
                    )

            ## add measurement line
            if self.measureID == 2:
                frame = cv2.line(frame, (self.cursorx0, self.cursory0), (self.cursorxlive, self.cursorylive), (0, 0, int(0.6*255)), 2 )

                # now we generate the displayed text
                if self.measurescale == 0 or (self.measurescale != 0 and self.objID == 0) or (self.measurescale != 0 and self.telID == 0):   # check if we want to measure pixels or µm
                    measlen = np.sqrt( (self.cursorxlive-self.cursorx0)**2 + (self.cursorylive-self.cursory0)**2 ) # pixel distance
                    distlabel = "length: {:.2f}px".format(measlen)
                elif self.measurescale == 1 and self.objID != 0:
                    measlen = np.sqrt( (self.cursorxlive-self.cursorx0)**2 + (self.cursorylive-self.cursory0)**2 ) # pixel distance
                    scale = float(self.ui.lineEdit_pxlen.text()) / self.micobjmags[self.objID]
                    distlabel = "length: {:.2f}um".format(measlen*scale)
                elif self.measurescale == 2 and self.telID != 0:
                    dx = np.abs(self.cursorx0 - self.cursorxlive)
                    dy = np.abs(self.cursory0 - self.cursorylive)
                    dalpharad = np.arctan(float(self.ui.lineEdit_pxlen.text())/1000 * np.sqrt(dx**2 + dy**2) / self.telfocal[self.telID])
                    arcsec = dalpharad/(2*np.pi)*360 * 3600  # first in deg then times 60x60 for bogsec
                    m = np.floor(arcsec/60)
                    s = arcsec % 60
                    distlabel = "size: " + "{:.0f}".format(m) +"\"" "{:.1f}".format(s) + "'"

                frame = cv2.putText(
                    frame,
                    text = distlabel,
                    org = (self.cursorxlive + 28, self.cursorylive - 15),
                    fontFace = cv2.FONT_HERSHEY_DUPLEX,
                    fontScale = 1.0,
                    color = (0, 0, 0.6*255),
                    thickness = 1
                    )
                



            elif self.measureID == 3:
                frame = cv2.line(frame, (self.cursorx0, self.cursory0), (self.cursorx1, self.cursory1), (0, 0, int(0.6*255)), 2 )
                
                # now we generate the displayed text
                if self.measurescale == 0 or (self.measurescale != 0 and self.objID == 0) or (self.measurescale != 0 and self.telID == 0):   # check if we want to measure pixels or µm
                    measlen = np.sqrt( (self.cursorx1-self.cursorx0)**2 + (self.cursory1-self.cursory0)**2 ) # pixel distance
                    distlabel = "length: {:.2f}px".format(measlen)
                elif self.measurescale == 1 and self.objID != 0:
                    measlen = np.sqrt( (self.cursorx1-self.cursorx0)**2 + (self.cursory1-self.cursory0)**2 ) # pixel distance
                    scale = float(self.ui.lineEdit_pxlen.text()) / self.micobjmags[self.objID]
                    distlabel = "length: {:.2f}um".format(measlen*scale)
                elif self.measurescale == 2 and self.telID != 0:
                    dx = np.abs(self.cursorx0 - self.cursorx1)
                    dy = np.abs(self.cursory0 - self.cursory1)
                    dalpharad = np.arctan(float(self.ui.lineEdit_pxlen.text())/1000 * np.sqrt(dx**2 + dy**2) / self.telfocal[self.telID])
                    arcsec = dalpharad/(2*np.pi)*360 * 3600  # first in deg then times 60x60 for arcsec
                    m = np.floor(arcsec/60)
                    s = arcsec % 60
                    distlabel = "size: " + "{:.0f}".format(m) +"\"" "{:.1f}".format(s) + "'"
                
                frame = cv2.putText(
                    frame,
                    text = distlabel,
                    org = (self.cursorx1 + 28, self.cursory1 - 15),
                    fontFace = cv2.FONT_HERSHEY_DUPLEX,
                    fontScale = 1.0,
                    color = (0, 0, 0.6*255),
                    thickness = 1
                    )

            #now we keep the final image including all information    
            self.framesave = frame  # this is what will be saved, if we press the save button
            
            # in case we record a video
            if self.vidrec == True: # we want to create a video
                if self.ui.checkBox_timelapse.isChecked(): # we want to make a timelaps movie
                    if time.time() - self.vidtime1 > self.TLperiode: # now it is time to add a new frame
                        self.videoout.write(frame)
                        self.vidtime1 = time.time() # time when we took the last frame
                else: # standard video without timelapse
                    self.videoout.write(frame) # we add every image to movie

            # window preparation check 
            if self.videomin == False and self.recreatewin == False:   # we only show the image if the window is prepared and the window is not minimized
                cv2.imshow('live-view', frame) # we update the plot    
                cv2.setMouseCallback('live-view', self.mousemove_event)
    
            else:
                cv2.destroyAllWindows()
            
            
            key = cv2.waitKey(10) # is needed otherwise the image is not updated ... it needs some time
        
            # ways out of that loop and to finish the software in camera mode
            if key == 27:  # ways to finish the loop
                break
        
        # camera update loop finisehd so we have to reset the startup parameters and close the window
        self.recreatewin = True 
        cv2.destroyWindow('live-view')   # finally we close the window 

    def togglefreeeze(self):
        if self.runcam == True:
            if self.freeze == False:
                self.ui.pushButton_freeze.setStyleSheet(u""+ self.buttonstyle("play.png", "playb.png", 1)) # set to activated mode
            else:
                self.ui.pushButton_freeze.setStyleSheet(u""+ self.buttonstyle("pause.png", "pauseb.png", 0)) # set to unactivated mode
            
            self.freeze = not(self.freeze) # we just toggle the image freeze flag
        else:
            self.statusmessage("no camera connected")

    def recordvid(self): # if we want to record a video file
        
        if self.runcam == True: # camera is running
            if self.vidrec == False: # we want to start recording

                ## first we start doing what we always do ... create the filename and path
                if self.checksavefolder(1) and isinstance(self.TLperiode, float): # check forder and create or change it if necessary
                    #combine filename           
                    fpath = self.ui.lineEdit_filepath.text()
                    fname = self.ui.lineEdit_filename.text() 
                    imgnumber = self.ui.lineEdit_imgnumber.text()
                    fformat = 'avi'
    
                    #check if autoadd image number is checker
                    if self.ui.checkBox_autoaddimgnumber.isChecked() == False:
                        fullpath = fpath+"\\"+fname
                    elif self.ui.checkBox_autoaddimgnumber.isChecked() == True:
                        fullpath = fpath+"\\"+fname+imgnumber
                        # increase image number
                        self.ui.lineEdit_imgnumber.setText(str(int(imgnumber) + 1))
                    
                    # if we are in timelaps mode we store Period-information in filename
                    if self.ui.checkBox_timelapse.isChecked(): # we are in timelaps mode
                        fullpath = fullpath + "_TL" + str(self.TLperiode) + "sec" # here we add the info

                    # finally we add the filetype
                    fullpath = fullpath +"."+fformat

                    # now we can prepare the file where we want to store the video data
                    fourcc = cv2.VideoWriter_fourcc(*'XVID') # codec
                    self.messageemitter.sendmessage("start recording") # send message to status
                    self.ui.pushButton_record.setStyleSheet(u""+ self.buttonstyleREC("record.png", "recordb.png", 1)) # set to activated mode (button)
                    self.videoout = cv2.VideoWriter(fullpath, fourcc, 20.0, (self.resolution[0], self.resolution[1]))
                    self.vidtime0 = time.time() # we store the time when we started recording
                    self.vidrec = True # set flag for recording
                else:
                    self.statusmessage("settings error")
            else: # we want to stop recording
                self.vidrec = False
                time.sleep(0.25) # we give the loop again some time
                self.messageemitter.sendmessage("stopped recording")
                self.videoout.release() # we release the file
                self.ui.pushButton_record.setStyleSheet(u""+ self.buttonstyleREC("record.png", "recordb.png", 0)) # set to activated mode (button)
                time.sleep(0.15) # and we wait for a short time


        else: # no camera connected so we cannot record anything
            self.statusmessage("no camera connected")

    def mousemove_event(self, event, x, y, flags, params):
       
        # this here we can do always    
        if event == cv2.EVENT_MOUSEMOVE:  # if mouse is mopving update livecursor
            self.cursorxlive = x
            self.cursorylive = y

        if event == cv2.EVENT_LBUTTONDOWN: # if clicked, keep clicked coordinates
            if self.measureID == 1: # this we do, if we started to measure a distance
                self.cursorx0 = x
                self.cursory0 = y
                self.measureID = 2
                self.statusmessage("set second point")    
            elif self.measureID == 2:
                self.cursorx1 = x
                self.cursory1 = y
                self.measureID = 3
                self.ui.pushButton_measure.setEnabled(True)
            elif self.measureID == 3:
                self.cursorx0 = x
                self.cursory0 = y
                self.measureID = 2 # we start a new measurment at current position and wait for end-point
                #self.measure() # we do the same as if we would press the clear/measurement button
        

    def measure(self):
        if self.runcam == True: # only if we have a running camera
            
            if self.measureID == 1 or self.measureID == 2 or self.measureID == 3: # if we are in a measurement when the button is clicked, then close measurement
                self.measureID = 0 # this will reset the measurement (see following if condition otherwise we would ne to have elif)
                self.ui.pushButton_measure.setStyleSheet(u""+ self.buttonstyle("measure.png", "measureb.png", 0)) # set to unactivated mode
            elif self.measureID == 0: # else we start the measurement mode
                self.measureID = 1 # and begin with point one
                self.ui.pushButton_measure.setStyleSheet(u""+ self.buttonstyle("measure.png", "measureb.png", 1)) # set to activated mode
                self.statusmessage("set first point")
                                 
        else: # if camera is not running send status
            self.statusmessage('no camera connected')


    def imagemani(self, frame):             # this manipulates the frame and flips the x od/and y axis
        # flip x and y
        if self.freeze == True:
            frame = cv2.flip(cv2.flip(frame,1),1) # only in freeze mode we need this doubleflip to update something in the cv2 environement ... just replacing the frame data with the stored frame is not enough .. i have no idea why

        if self.ui.checkBox_flipx.isChecked():      
            frame = cv2.flip(frame,1)
        if self.ui.checkBox_flipy.isChecked():
            frame = cv2.flip(frame,0)

        # live view image processing
        if  self.ui.checkBox_applyimageman.isChecked():
            
            # image lightness and saturation modification
            hls_frame = frameenhanced = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS)

            # adaptive histogram equalization
            if self.ui.checkBox_ace.isChecked():
                framebw = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)   # grayscale image
                clahe = cv2.createCLAHE(clipLimit=self.contrast/10, tileGridSize=(self.contrast2, self.contrast2))
                frameenhanced[:,:,1] = clahe.apply(framebw)
                frameenhanced[:, :, 2] = np.clip(self.saturation * frameenhanced[:, :, 2], 0, 255)
                frameenhanced[:, :, 1] = np.clip(self.lightness * frameenhanced[:, :, 1], 0, 255)
                frame = cv2.cvtColor(frameenhanced, cv2.COLOR_HLS2BGR) 

            else:
                # image lightness and saturation modification
                hls_frame[:, :, 2] = np.clip(self.saturation * hls_frame[:, :, 2], 0, 255)
                hls_frame[:, :, 1] = np.clip(self.lightness * hls_frame[:, :, 1], 0, 255)
                frame = cv2.cvtColor(hls_frame, cv2.COLOR_HLS2BGR)      

            if self.ui.checkBox_autostretch.isChecked() or self.ui.checkBox_offsetsub.isChecked():
                frmin = np.min(frame)
                frmax = np.max(frame)
                if self.ui.checkBox_autostretch.isChecked():
                    m = 254/(frmax - frmin) # slope                
                    off = -m*frmin
                    frame = np.uint8(m*frame + off)
                else:
                    frame = frame - frmin


            if self.ui.checkBox_invert.isChecked():
                frame = cv2.bitwise_not(frame)



        return np.uint8(frame)                        # give back the image

    def setexposuretime(self):  # update exposure time
        self.ui.label_exposure.setText(str(self.ui.horizontalSlider_exposure.value()))
        if self.runcam == True:
            self.mycam.set(cv2.CAP_PROP_EXPOSURE, self.ui.horizontalSlider_exposure.value())

    def setbrightness(self):    # update brightness (not sure if that makes any sense)
        self.ui.label_bright.setText(str(self.ui.horizontalSlider_bright.value()))
        if self.runcam == True:
            self.mycam.set(cv2.CAP_PROP_BRIGHTNESS, self.ui.horizontalSlider_bright.value())

    def setgain(self):
        self.ui.label_aver.setText(str(self.ui.horizontalSlider_gain.value()))
        if self.runcam == True:
            self.mycam.set(cv2.CAP_PROP_GAIN , self.ui.horizontalSlider_gain.value())

    def getdatabase(self):
        
        self.micobjnames = ["measure Pixels"]   # prepare list for objective names
        self.micobjmags = [1]    # prepare list for objective magnifications
        
        if fileexists('confs/objectives.csv'): # only if file exists
            with open('confs/objectives.csv') as csvdatabase:    # read database
                objdatabase = csv.reader(csvdatabase)
                rowid = 0
                for row in objdatabase:
                    if rowid != 0:
                        self.micobjmags.append(float(row[0]))   # fill in mags in list
                        self.micobjnames.append(str(row[0])+"X - " + str(row[1]))  # fill in names in list
                    rowid += 1 # goto next line in database list
        else:
            self.messageemitter.sendmessage("database missing") # and send statusmessage

        self.ui.comboBox_micobject.clear()
        self.ui.comboBox_micobject.addItems(self.micobjnames)

        # now we do the same with telescopes/focal lenghts
        self.telnames = ["measure Pixels"]   # prepare list for objective names
        self.telfocal = [1]    # prepare list for objective magnifications
        
        if fileexists('confs/telescopes.csv'): # only if file exists
            with open('confs/telescopes.csv') as csvdatabase:    # read database
                objdatabase = csv.reader(csvdatabase)
                rowid = 0
                for row in objdatabase:
                    if rowid != 0:
                        self.telfocal.append(float(row[0]))   # fill in mags in list
                        self.telnames.append(str(row[0])+"mm - " + str(row[1]))  # fill in names in list
                    rowid += 1 # goto next line in database list
        else:
            self.messageemitter.sendmessage("database missing") # and send statusmessage

        self.ui.comboBox_telescopes.clear()
        self.ui.comboBox_telescopes.addItems(self.telnames)

    def averager(self):
        if self.runcam == True:
            # this here only handels the button appearance and sets the averagemode-flag
            if self.averagemode == False:
                self.averagemode = True # first we set tha flag
                self.ui.pushButton_average.setStyleSheet(u""+ self.buttonstyle("summe.png", "summeb.png", 1)) # set to activated mode

            else:
                self.averagemode = False # first we set tha flag
                time.sleep(0.25)
                self.ui.pushButton_average.setStyleSheet(u""+ self.buttonstyle("summe.png", "summeb.png", 0)) # set to unactivated mode
                self.avID = 0 # we reset the averager ID to 0 so that we can start from scratch
        else:
            self.statusmessage("no camera connected")

    def checkframeaveragenumber(self):
        input = self.ui.lineEdit_frameavnum.text()
        if input.isdigit():
            if int(input) > 0:
                self.avID = 0
                self.averagenum = int(input)
            else: 
                self.statusmessage("invalid average number")

                if self.averagemode == True:
                    self.averager() # if we are in averager mode stop it
                else:
                    pass
        else:
            self.statusmessage("invalid average number")
            if self.averagemode == True:
                self.averager() # if we are in averager mode stop it
            else:
                pass

    def checkTperiod(self):
        try:
            self.TLperiode = float(self.ui.lineEdit_Ttimelaps.text())
        except:
            self.statusmessage("invalid value")


    def imagepara(self):

        if self.settingsopen == True:
            self.opensettings()     #   if the settings are open, simply turn them off

        if self.imageparaopen == False: 
            self.ui.pushButton_imagepara.setStyleSheet(u""+ self.buttonstyle("image.png", "imageb.png", 1)) # set to activated mode
            self.ui.stackedWidget_settings.setCurrentIndex(1)
            self.imageparaopen = True
            
        else:
            self.ui.pushButton_imagepara.setStyleSheet(u""+ self.buttonstyle("image.png", "imageb.png", 0)) # set to unactivated mode
            self.imageparaopen = False
        self.menusetup()


        
####################################################################### liveview ##############################################################
 
    def setlightness(self):
        self.lightness = round(1 + (int(self.ui.horizontalSlider_lightness.value()-12))/25, 2)
        self.ui.label_lightness.setText("{:.2f}".format(self.lightness))

    def setsaturation(self):
        self.saturation = round(1 + (int(self.ui.horizontalSlider_saturation.value()-50))/50, 2)
        self.ui.label_saturation.setText("{:.2f}".format(self.saturation))

    def setcontrast(self):
        self.contrast = float(self.ui.horizontalSlider_contrastamp.value())
        self.contrast2 = int(self.ui.horizontalSlider_contrastgrid.value())
        self.ui.label_contrast.setText("{:.0f}".format(self.contrast))
        self.ui.label_contrast_2.setText("{:.0f}".format(self.contrast2))


#################################################### save image ########################################################

    def browsefiles(self):  # open browse window to define saving path
        path = QFileDialog.getExistingDirectory(self, "Open file")
        self.ui.lineEdit_filepath.setText(path)

    def clicksaveimg(self):         # save image
        if self.runcam == True:
            frame = self.framesave
            #combine filename
            if self.checksavefolder(1): # check forder and create or change it if necessary
                fpath = self.ui.lineEdit_filepath.text()
                fname = self.ui.lineEdit_filename.text()
                fformat = self.ui.lineEdit_imgformat.text()
                imgnumber = self.ui.lineEdit_imgnumber.text()
            
                #check if autoadd image number is checker
                if self.ui.checkBox_autoaddimgnumber.isChecked() == False:
                    fullpath = fpath+"\\"+fname+"."+fformat
                elif self.ui.checkBox_autoaddimgnumber.isChecked() == True:
                    fullpath = fpath+"\\"+fname+imgnumber+"."+fformat
                    # increase image number
                    self.ui.lineEdit_imgnumber.setText(str(int(imgnumber) + 1))
                
                # now save that thing
                cv2.imwrite(fullpath, frame)
                self.messageemitter.sendmessage("image saved")
            else:
                self.statusmessage("save settings error!")
            
        else:
            self.statusmessage("no camera connected")



##############################################################################################################################################
#                                                          SETTINGS WINDOW
##############################################################################################################################################

class Fakeparentwin():
    def __init__(self):
        self.intwinpos = [100, 10]


##  start gui
if __name__ == "__main__":
    app = QApplication(sys.argv)              # define Qapplication Object
    fakeparentwin = Fakeparentwin()           # that everything is fine and prepared for printedLAB Labcontrol (interface)
    experimentUI = camwin(0,fakeparentwin)    # define User interface
    app.exec()                                # execute
    sys.exit(print("code finished"))          # exit code