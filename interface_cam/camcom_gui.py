# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'camcom_gui.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSlider, QStackedWidget, QWidget)
import graphics.buttons_rc

class Ui_camcom_mainwin(object):
    def setupUi(self, camcom_mainwin):
        if not camcom_mainwin.objectName():
            camcom_mainwin.setObjectName(u"camcom_mainwin")
        camcom_mainwin.resize(442, 760)
        camcom_mainwin.setStyleSheet(u"button->setStyleSheet(\"border-image:url(:/icons/arrow_l.png);\");")
        self.frame = QFrame(camcom_mainwin)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 10, 441, 746))
        self.frame.setStyleSheet(u"background-color: rgb(50, 49, 52);\n"
"border-radius: 0px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setEnabled(False)
        self.label.setGeometry(QRect(10, 5, 141, 31))
        self.label.setStyleSheet(u"background-color: transparent;\n"
"border: none;")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(-10, 40, 791, 51))
        self.frame_2.setStyleSheet(u"border-radius: 0px;\n"
"border: 3px solid rgba(0, 0, 0, 50);\n"
"background-color: rgba(0, 0, 0, 50);\n"
"\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.comboBox_camport = QComboBox(self.frame_2)
        self.comboBox_camport.setObjectName(u"comboBox_camport")
        self.comboBox_camport.setGeometry(QRect(100, 15, 111, 22))
        self.comboBox_camport.setStyleSheet(u"color: rgb(220,220,220)\n"
"")
        self.pushButton_comrefresh = QPushButton(self.frame_2)
        self.pushButton_comrefresh.setObjectName(u"pushButton_comrefresh")
        self.pushButton_comrefresh.setGeometry(QRect(220, 12, 101, 31))
        self.pushButton_comrefresh.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	background-color: rgb(50, 50, 50);\n"
"	color: rgb(220,220,220);\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(100, 150, 200);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(130, 180, 230);\n"
"	color: white;\n"
"}")
        self.pushButton_comconnect = QPushButton(self.frame_2)
        self.pushButton_comconnect.setObjectName(u"pushButton_comconnect")
        self.pushButton_comconnect.setGeometry(QRect(330, 12, 101, 31))
        self.pushButton_comconnect.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	background-color: rgb(50, 50, 50);\n"
"	color: rgb(220,220,220);\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(100, 150, 200);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(130, 180, 230);\n"
"	color: white;\n"
"}")
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(16, 10, 81, 31))
        self.label_4.setStyleSheet(u"background-color: transparent;\n"
"border-color: transparent;")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.pushButton_screenmode = QPushButton(self.frame)
        self.pushButton_screenmode.setObjectName(u"pushButton_screenmode")
        self.pushButton_screenmode.setGeometry(QRect(385, 10, 20, 20))
        self.pushButton_screenmode.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	background-color: rgb(100,100,100);\n"
"	background-image: url(:/icons/screenmode.png);\n"
"	color: white;\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(100, 150, 200);\n"
"	color: white;\n"
"}\n"
"\n"
"")
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(-5, 460, 791, 51))
        self.frame_4.setStyleSheet(u"border-radius: 0px;\n"
"border: 3px solid rgba(0, 0, 0, 50);\n"
"background-color: rgba(0, 0, 0, 50);\n"
"\n"
"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.pushButton_settings = QPushButton(self.frame_4)
        self.pushButton_settings.setObjectName(u"pushButton_settings")
        self.pushButton_settings.setGeometry(QRect(25, 10, 30, 31))
        self.pushButton_settings.setToolTipDuration(3)
        self.pushButton_settings.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	background-color: rgb(90, 90, 90);\n"
"	background-image: url(:/icons/settings.png);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-image: url(:/icons/settingsb.png);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(130, 180, 230);\n"
"	color: white;\n"
"}")
        self.pushButton_settings.setCheckable(False)
        self.pushButton_measure = QPushButton(self.frame_4)
        self.pushButton_measure.setObjectName(u"pushButton_measure")
        self.pushButton_measure.setGeometry(QRect(180, 10, 31, 31))
        self.pushButton_measure.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	background-color: rgb(90, 90, 90);\n"
"	background-image: url(:/icons/measure.png);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-image: url(:/icons/measureb.png);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(130, 180, 230);\n"
"	color: white;\n"
"}")
        self.pushButton_measure.setCheckable(False)
        self.pushButton_saveimg = QPushButton(self.frame_4)
        self.pushButton_saveimg.setObjectName(u"pushButton_saveimg")
        self.pushButton_saveimg.setGeometry(QRect(370, 10, 61, 31))
        self.pushButton_saveimg.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	background-color: rgb(120,0,0);\n"
"	background-image: url(:/icons/takeimage.png);\n"
"	color: white;\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 0, 0);\n"
"	color: white;\n"
"}\n"
"\n"
"")
        self.pushButton_saveimg.setCheckable(False)
        self.pushButton_record = QPushButton(self.frame_4)
        self.pushButton_record.setObjectName(u"pushButton_record")
        self.pushButton_record.setGeometry(QRect(300, 10, 61, 31))
        self.pushButton_record.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	background-color: rgb(90, 90, 90);\n"
"	background-image: url(:/icons/record.png);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-image: url(:/icons/recordb.png);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 0, 0);\n"
"	color: white;\n"
"}")
        self.pushButton_record.setCheckable(False)
        self.pushButton_freeze = QPushButton(self.frame_4)
        self.pushButton_freeze.setObjectName(u"pushButton_freeze")
        self.pushButton_freeze.setGeometry(QRect(220, 10, 31, 31))
        self.pushButton_freeze.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	background-color: rgb(90, 90, 90);\n"
"	background-image: url(:/icons/pause.png);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-image: url(:/icons/pauseb.png);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(130, 180, 230);\n"
"	color: white;\n"
"}")
        self.pushButton_freeze.setCheckable(False)
        self.pushButton_average = QPushButton(self.frame_4)
        self.pushButton_average.setObjectName(u"pushButton_average")
        self.pushButton_average.setGeometry(QRect(260, 10, 31, 31))
        self.pushButton_average.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	background-color: rgb(90, 90, 90);\n"
"	background-image: url(:/icons/summe.png);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-image: url(:/icons/summeb.png);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(130, 180, 230);\n"
"	color: white;\n"
"}")
        self.pushButton_average.setCheckable(False)
        self.label_19 = QLabel(self.frame_4)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(55, 15, 50, 21))
        self.label_19.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"color: rgb(220,220,220);\n"
"\n"
"")
        self.label_19.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)
        self.label_19.setWordWrap(False)
        self.pushButton_imagepara = QPushButton(self.frame_4)
        self.pushButton_imagepara.setObjectName(u"pushButton_imagepara")
        self.pushButton_imagepara.setGeometry(QRect(140, 10, 31, 31))
        self.pushButton_imagepara.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	background-color: rgb(90, 90, 90);\n"
"	background-image: url(:/icons/image.png);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-image: url(:/icons/imageb.png);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(130, 180, 230);\n"
"	color: white;\n"
"}")
        self.pushButton_imagepara.setCheckable(False)
        self.checkBox_imginfo = QCheckBox(self.frame)
        self.checkBox_imginfo.setObjectName(u"checkBox_imginfo")
        self.checkBox_imginfo.setGeometry(QRect(331, 195, 101, 31))
        self.checkBox_imginfo.setStyleSheet(u"QCheckBox {\n"
"	\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: none;\n"
"	color: rgb(220,220,220);\n"
"}")
        self.checkBox_flipx = QCheckBox(self.frame)
        self.checkBox_flipx.setObjectName(u"checkBox_flipx")
        self.checkBox_flipx.setGeometry(QRect(131, 195, 80, 31))
        self.checkBox_flipx.setStyleSheet(u"QCheckBox {\n"
"	\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: none;\n"
"	color: rgb(220,220,220);\n"
"}")
        self.label_aver = QLabel(self.frame)
        self.label_aver.setObjectName(u"label_aver")
        self.label_aver.setGeometry(QRect(391, 165, 31, 21))
        self.label_aver.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(0, 0, 0, 50);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"color: rgb(220,220,220);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_aver.setAlignment(Qt.AlignCenter)
        self.horizontalSlider_bright = QSlider(self.frame)
        self.horizontalSlider_bright.setObjectName(u"horizontalSlider_bright")
        self.horizontalSlider_bright.setGeometry(QRect(100, 135, 281, 22))
        self.horizontalSlider_bright.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: 1px solid black;\n"
"    height: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"    margin: 2px 0;\n"
"	background: rgba(100, 150, 200,50);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: rgb(100,150,200);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 18px;\n"
"    margin: -2px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"    border-radius: 3px;\n"
"}")
        self.horizontalSlider_bright.setMinimum(0)
        self.horizontalSlider_bright.setMaximum(100)
        self.horizontalSlider_bright.setValue(50)
        self.horizontalSlider_bright.setOrientation(Qt.Horizontal)
        self.horizontalSlider_bright.setInvertedAppearance(False)
        self.label_15 = QLabel(self.frame)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(25, 135, 81, 21))
        self.label_15.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.label_bright = QLabel(self.frame)
        self.label_bright.setObjectName(u"label_bright")
        self.label_bright.setGeometry(QRect(391, 135, 31, 21))
        self.label_bright.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(0, 0, 0, 50);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"color: rgb(220,220,220);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_bright.setAlignment(Qt.AlignCenter)
        self.checkBox_flipy = QCheckBox(self.frame)
        self.checkBox_flipy.setObjectName(u"checkBox_flipy")
        self.checkBox_flipy.setGeometry(QRect(231, 195, 80, 31))
        self.checkBox_flipy.setStyleSheet(u"QCheckBox {\n"
"	\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: none;\n"
"	color: rgb(220,220,220);\n"
"}")
        self.horizontalSlider_gain = QSlider(self.frame)
        self.horizontalSlider_gain.setObjectName(u"horizontalSlider_gain")
        self.horizontalSlider_gain.setGeometry(QRect(100, 165, 281, 22))
        self.horizontalSlider_gain.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: 1px solid black;\n"
"    height: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"    margin: 2px 0;\n"
"	background: rgba(100, 150, 200,50);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: rgb(100,150,200);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 18px;\n"
"    margin: -2px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"    border-radius: 3px;\n"
"}")
        self.horizontalSlider_gain.setMinimum(0)
        self.horizontalSlider_gain.setMaximum(100)
        self.horizontalSlider_gain.setValue(0)
        self.horizontalSlider_gain.setOrientation(Qt.Horizontal)
        self.horizontalSlider_gain.setInvertedAppearance(False)
        self.label_14 = QLabel(self.frame)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(25, 105, 71, 21))
        self.label_14.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.label_16 = QLabel(self.frame)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(25, 165, 61, 21))
        self.label_16.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.checkBox_grayscale = QCheckBox(self.frame)
        self.checkBox_grayscale.setObjectName(u"checkBox_grayscale")
        self.checkBox_grayscale.setGeometry(QRect(31, 195, 80, 31))
        self.checkBox_grayscale.setStyleSheet(u"QCheckBox {\n"
"	\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: none;\n"
"color: rgb(220,220,220);\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"}")
        self.label_exposure = QLabel(self.frame)
        self.label_exposure.setObjectName(u"label_exposure")
        self.label_exposure.setGeometry(QRect(391, 105, 31, 21))
        self.label_exposure.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(0, 0, 0, 50);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"color: rgb(220,220,220);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_exposure.setAlignment(Qt.AlignCenter)
        self.horizontalSlider_exposure = QSlider(self.frame)
        self.horizontalSlider_exposure.setObjectName(u"horizontalSlider_exposure")
        self.horizontalSlider_exposure.setGeometry(QRect(100, 105, 281, 22))
        self.horizontalSlider_exposure.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: 1px solid black;\n"
"    height: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"    margin: 2px 0;\n"
"	background: rgba(100, 150, 200,50);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: rgb(100,150,200);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 18px;\n"
"    margin: -2px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"    border-radius: 3px;\n"
"}")
        self.horizontalSlider_exposure.setMinimum(-14)
        self.horizontalSlider_exposure.setMaximum(-4)
        self.horizontalSlider_exposure.setValue(-8)
        self.horizontalSlider_exposure.setSliderPosition(-8)
        self.horizontalSlider_exposure.setOrientation(Qt.Horizontal)
        self.horizontalSlider_exposure.setInvertedAppearance(False)
        self.horizontalSlider_exposure.setInvertedControls(False)
        self.label_status = QLabel(self.frame)
        self.label_status.setObjectName(u"label_status")
        self.label_status.setGeometry(QRect(155, 5, 191, 31))
        self.label_status.setStyleSheet(u"background-color: transparent;\n"
"border-color: transparent;")
        self.label_status.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.pushButton_mini = QPushButton(self.frame)
        self.pushButton_mini.setObjectName(u"pushButton_mini")
        self.pushButton_mini.setGeometry(QRect(360, 10, 20, 20))
        font = QFont()
        font.setFamilies([u"MS Shell Dlg 2"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.pushButton_mini.setFont(font)
        self.pushButton_mini.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	background-color: rgb(100,100,100);\n"
"	background-image: url(:/icons/minimize.png);\n"
"	color: white;\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(100, 150, 200);\n"
"	color: white;\n"
"}\n"
"\n"
"")
        self.stackedWidget_scopetype = QStackedWidget(self.frame)
        self.stackedWidget_scopetype.setObjectName(u"stackedWidget_scopetype")
        self.stackedWidget_scopetype.setGeometry(QRect(0, 290, 441, 161))
        self.stackedWidget_scopetype.setStyleSheet(u"")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.comboBox_illumode = QComboBox(self.page)
        self.comboBox_illumode.setObjectName(u"comboBox_illumode")
        self.comboBox_illumode.setGeometry(QRect(190, 97, 231, 23))
        self.comboBox_illumode.setStyleSheet(u"border: 10px;\n"
"border-radius: 0px;\n"
"border-color: black;\n"
"background-color: rgba(120,120,120,50);\n"
"color:rgb(220,220,220);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_17 = QLabel(self.page)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(25, 67, 61, 21))
        self.label_17.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.label_bright_2 = QLabel(self.page)
        self.label_bright_2.setObjectName(u"label_bright_2")
        self.label_bright_2.setGeometry(QRect(391, 67, 31, 21))
        self.label_bright_2.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(0, 0, 0, 50);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"color: rgb(220,220,220);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_bright_2.setAlignment(Qt.AlignCenter)
        self.horizontalSlider_lampinten = QSlider(self.page)
        self.horizontalSlider_lampinten.setObjectName(u"horizontalSlider_lampinten")
        self.horizontalSlider_lampinten.setGeometry(QRect(100, 67, 281, 22))
        self.horizontalSlider_lampinten.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: 1px solid black;\n"
"    height: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"    margin: 2px 0;\n"
"	background: rgba(100, 150, 200,50);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: rgb(100,150,200);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 18px;\n"
"    margin: -2px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"    border-radius: 3px;\n"
"}")
        self.horizontalSlider_lampinten.setMinimum(0)
        self.horizontalSlider_lampinten.setMaximum(100)
        self.horizontalSlider_lampinten.setValue(100)
        self.horizontalSlider_lampinten.setOrientation(Qt.Horizontal)
        self.horizontalSlider_lampinten.setInvertedAppearance(False)
        self.label_18 = QLabel(self.page)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(25, 97, 131, 21))
        self.label_18.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.comboBox_micobject = QComboBox(self.page)
        self.comboBox_micobject.setObjectName(u"comboBox_micobject")
        self.comboBox_micobject.setGeometry(QRect(190, 127, 231, 23))
        self.comboBox_micobject.setStyleSheet(u"border: 10px;\n"
"border-radius: 0px;\n"
"border-color: black;\n"
"background-color: rgba(120,120,120,50);\n"
"color:rgb(220,220,220);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_20 = QLabel(self.page)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(25, 127, 161, 21))
        self.label_20.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.frame_6 = QFrame(self.page)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(10, 10, 421, 41))
        self.frame_6.setStyleSheet(u"border-radius: 0px;\n"
"border: 3px solid rgba(0, 0, 0, 30);\n"
"background-color: rgba(0, 0, 0, 30);\n"
"\n"
"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.comboBox_lampport = QComboBox(self.frame_6)
        self.comboBox_lampport.setObjectName(u"comboBox_lampport")
        self.comboBox_lampport.setGeometry(QRect(80, 10, 111, 22))
        self.comboBox_lampport.setStyleSheet(u"color: rgb(220,220,220)\n"
"")
        self.pushButton_lampconnect = QPushButton(self.frame_6)
        self.pushButton_lampconnect.setObjectName(u"pushButton_lampconnect")
        self.pushButton_lampconnect.setGeometry(QRect(310, 5, 101, 31))
        self.pushButton_lampconnect.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	background-color: rgb(50, 50, 50);\n"
"	color: rgb(220,220,220);\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(100, 150, 200);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(130, 180, 230);\n"
"	color: white;\n"
"}")
        self.label_5 = QLabel(self.frame_6)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 5, 51, 31))
        self.label_5.setStyleSheet(u"background-color: transparent;\n"
"border-color: transparent;")
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.pushButton_lamprefresh = QPushButton(self.frame_6)
        self.pushButton_lamprefresh.setObjectName(u"pushButton_lamprefresh")
        self.pushButton_lamprefresh.setGeometry(QRect(200, 5, 101, 31))
        self.pushButton_lamprefresh.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	background-color: rgb(50, 50, 50);\n"
"	color: rgb(220,220,220);\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(100, 150, 200);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(130, 180, 230);\n"
"	color: white;\n"
"}")
        self.stackedWidget_scopetype.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label_21 = QLabel(self.page_2)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(190, 55, 110, 21))
        self.label_21.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.comboBox_telescopes = QComboBox(self.page_2)
        self.comboBox_telescopes.setObjectName(u"comboBox_telescopes")
        self.comboBox_telescopes.setGeometry(QRect(190, 75, 231, 23))
        self.comboBox_telescopes.setStyleSheet(u"border: 10px;\n"
"border-radius: 0px;\n"
"border-color: black;\n"
"background-color: rgba(120,120,120,50);\n"
"color:rgb(220,220,220);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.frame_7 = QFrame(self.page_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(10, 10, 421, 41))
        self.frame_7.setStyleSheet(u"border-radius: 0px;\n"
"border: 3px solid rgba(0, 0, 0, 30);\n"
"background-color: rgba(0, 0, 0, 30);\n"
"\n"
"")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.comboBox_mountport = QComboBox(self.frame_7)
        self.comboBox_mountport.setObjectName(u"comboBox_mountport")
        self.comboBox_mountport.setGeometry(QRect(80, 10, 111, 22))
        self.comboBox_mountport.setStyleSheet(u"color: rgb(220, 220,220)\n"
"")
        self.pushButton_mountconnect = QPushButton(self.frame_7)
        self.pushButton_mountconnect.setObjectName(u"pushButton_mountconnect")
        self.pushButton_mountconnect.setGeometry(QRect(310, 5, 101, 31))
        self.pushButton_mountconnect.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	background-color: rgb(50, 50, 50);\n"
"	color: rgb(220,220,220);\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(100, 150, 200);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(130, 180, 230);\n"
"	color: white;\n"
"}")
        self.pushButton_mountconnect.setCheckable(False)
        self.label_6 = QLabel(self.frame_7)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 5, 71, 31))
        self.label_6.setStyleSheet(u"background-color: transparent;\n"
"border-color: transparent;")
        self.label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.pushButton_mountrefresh = QPushButton(self.frame_7)
        self.pushButton_mountrefresh.setObjectName(u"pushButton_mountrefresh")
        self.pushButton_mountrefresh.setGeometry(QRect(200, 5, 101, 31))
        self.pushButton_mountrefresh.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	background-color: rgb(50, 50, 50);\n"
"	color: rgb(220,220,220);\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(100, 150, 200);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(130, 180, 230);\n"
"	color: white;\n"
"}")
        self.pushButton_freeze_2 = QPushButton(self.page_2)
        self.pushButton_freeze_2.setObjectName(u"pushButton_freeze_2")
        self.pushButton_freeze_2.setGeometry(QRect(70, 56, 41, 31))
        self.pushButton_freeze_2.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	background-color: rgba(90, 90, 90,0);\n"
"	background-image: url(:/icons/up.png);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-image: url(:/icons/upb.png);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-image: url(:/icons/upbb.png);\n"
"	color: white;\n"
"}")
        self.pushButton_freeze_2.setCheckable(False)
        self.pushButton_freeze_3 = QPushButton(self.page_2)
        self.pushButton_freeze_3.setObjectName(u"pushButton_freeze_3")
        self.pushButton_freeze_3.setGeometry(QRect(70, 130, 41, 31))
        self.pushButton_freeze_3.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	background-color: rgba(90, 90, 90,0);\n"
"	background-image: url(:/icons/dw.png);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-image: url(:/icons/dwb.png);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-image: url(:/icons/dwbb.png);\n"
"	color: white;\n"
"}")
        self.pushButton_freeze_3.setCheckable(False)
        self.pushButton_freeze_4 = QPushButton(self.page_2)
        self.pushButton_freeze_4.setObjectName(u"pushButton_freeze_4")
        self.pushButton_freeze_4.setGeometry(QRect(38, 88, 31, 41))
        self.pushButton_freeze_4.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	background-color: rgba(90, 90, 90,0);\n"
"	background-image: url(:/icons/le.png);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-image: url(:/icons/leb.png);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-image: url(:/icons/lebb.png);\n"
"	color: white;\n"
"}")
        self.pushButton_freeze_4.setCheckable(False)
        self.pushButton_freeze_5 = QPushButton(self.page_2)
        self.pushButton_freeze_5.setObjectName(u"pushButton_freeze_5")
        self.pushButton_freeze_5.setGeometry(QRect(112, 88, 31, 41))
        self.pushButton_freeze_5.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	background-color: rgba(90, 90, 90,0);\n"
"	background-image: url(:/icons/ri.png);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-image: url(:/icons/rib.png);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-image: url(:/icons/ribb.png);\n"
"	color: white;\n"
"}")
        self.pushButton_freeze_5.setCheckable(False)
        self.checkBox_tracking = QCheckBox(self.page_2)
        self.checkBox_tracking.setObjectName(u"checkBox_tracking")
        self.checkBox_tracking.setGeometry(QRect(190, 105, 231, 17))
        self.checkBox_tracking.setStyleSheet(u"QCheckBox {\n"
"	\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: none;\n"
"	color: rgb(220,220,220);\n"
"}")
        self.checkBox_tracking.setChecked(False)
        self.horizontalSlider_mountspeed = QSlider(self.page_2)
        self.horizontalSlider_mountspeed.setObjectName(u"horizontalSlider_mountspeed")
        self.horizontalSlider_mountspeed.setGeometry(QRect(285, 135, 101, 22))
        self.horizontalSlider_mountspeed.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: 1px solid black;\n"
"    height: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"    margin: 2px 0;\n"
"	background: rgba(100, 150, 200,50);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: rgb(100,150,200);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 18px;\n"
"    margin: -2px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"    border-radius: 3px;\n"
"}")
        self.horizontalSlider_mountspeed.setMinimum(1)
        self.horizontalSlider_mountspeed.setMaximum(5)
        self.horizontalSlider_mountspeed.setValue(3)
        self.horizontalSlider_mountspeed.setSliderPosition(3)
        self.horizontalSlider_mountspeed.setOrientation(Qt.Horizontal)
        self.horizontalSlider_mountspeed.setInvertedAppearance(False)
        self.horizontalSlider_mountspeed.setInvertedControls(False)
        self.label_37 = QLabel(self.page_2)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(190, 135, 91, 21))
        self.label_37.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.label_37.setWordWrap(False)
        self.label_mountspeed = QLabel(self.page_2)
        self.label_mountspeed.setObjectName(u"label_mountspeed")
        self.label_mountspeed.setGeometry(QRect(390, 135, 31, 21))
        self.label_mountspeed.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(0, 0, 0, 50);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"color: rgb(220,220,220);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_mountspeed.setAlignment(Qt.AlignCenter)
        self.stackedWidget_scopetype.addWidget(self.page_2)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.label_36 = QLabel(self.page_5)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(10, -10, 421, 181))
        self.label_36.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.label_36.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.stackedWidget_scopetype.addWidget(self.page_5)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(-10, 240, 791, 51))
        self.frame_3.setStyleSheet(u"border-radius: 0px;\n"
"border: 3px solid rgba(0, 0, 0, 50);\n"
"background-color: rgba(0, 0, 0, 50);\n"
"\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.pushButton_micmode = QPushButton(self.frame_3)
        self.pushButton_micmode.setObjectName(u"pushButton_micmode")
        self.pushButton_micmode.setGeometry(QRect(30, 10, 91, 31))
        self.pushButton_micmode.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	background-color: rgb(90, 90, 90);\n"
"	color: rgb(220,220,220);\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(130, 180, 230);\n"
"	color: white;\n"
"}")
        self.pushButton_telmode = QPushButton(self.frame_3)
        self.pushButton_telmode.setObjectName(u"pushButton_telmode")
        self.pushButton_telmode.setGeometry(QRect(130, 10, 91, 31))
        self.pushButton_telmode.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	background-color: rgb(90, 90, 90);\n"
"	color: rgb(220,220,220);\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(130, 180, 230);\n"
"	color: white;\n"
"}")
        self.pushButton_infobox = QPushButton(self.frame_3)
        self.pushButton_infobox.setObjectName(u"pushButton_infobox")
        self.pushButton_infobox.setGeometry(QRect(400, 10, 31, 31))
        self.pushButton_infobox.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	background-color: rgb(90, 90, 90);\n"
"	background-image: url(:/icons/info.png);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-image: url(:/icons/infob.png);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(130, 180, 230);\n"
"	color: white;\n"
"}")
        self.stackedWidget_settings = QStackedWidget(self.frame)
        self.stackedWidget_settings.setObjectName(u"stackedWidget_settings")
        self.stackedWidget_settings.setGeometry(QRect(0, 510, 441, 251))
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.lineEdit_imgformat = QLineEdit(self.page_3)
        self.lineEdit_imgformat.setObjectName(u"lineEdit_imgformat")
        self.lineEdit_imgformat.setGeometry(QRect(180, 130, 31, 23))
        self.lineEdit_imgformat.setStyleSheet(u"border: 10px;\n"
"border-radius: 0px;\n"
"border-color: black;\n"
"background-color: rgba(120,120,120,50);\n"
"color:rgb(220,220,220);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_25 = QLabel(self.page_3)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(25, 40, 161, 21))
        self.label_25.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.label_25.setWordWrap(False)
        self.label_23 = QLabel(self.page_3)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(170, 130, 16, 21))
        self.label_23.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.lineEdit_frameavnum = QLineEdit(self.page_3)
        self.lineEdit_frameavnum.setObjectName(u"lineEdit_frameavnum")
        self.lineEdit_frameavnum.setEnabled(True)
        self.lineEdit_frameavnum.setGeometry(QRect(180, 10, 41, 23))
        self.lineEdit_frameavnum.setStyleSheet(u"border: 10px;\n"
"border-radius: 0px;\n"
"border-color: black;\n"
"background-color: rgba(120,120,120,50);\n"
"color:rgb(220,220,220);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.lineEdit_frameavnum.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEdit_filename = QLineEdit(self.page_3)
        self.lineEdit_filename.setObjectName(u"lineEdit_filename")
        self.lineEdit_filename.setGeometry(QRect(25, 130, 113, 23))
        self.lineEdit_filename.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit_filename.setStyleSheet(u"border: 10px;\n"
"border-radius: 0px;\n"
"border-color: black;\n"
"background-color: rgba(120,120,120,50);\n"
"color:rgb(220,220,220);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.lineEdit_filename.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEdit_filepath = QLineEdit(self.page_3)
        self.lineEdit_filepath.setObjectName(u"lineEdit_filepath")
        self.lineEdit_filepath.setGeometry(QRect(130, 160, 281, 23))
        self.lineEdit_filepath.setStyleSheet(u"border: 10px;\n"
"border-radius: 0px;\n"
"border-color: black;\n"
"background-color: rgba(120,120,120,50);\n"
"color:rgb(220,220,220);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_27 = QLabel(self.page_3)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(25, 10, 161, 21))
        self.label_27.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.label_27.setWordWrap(False)
        self.lineEdit_pxlen = QLineEdit(self.page_3)
        self.lineEdit_pxlen.setObjectName(u"lineEdit_pxlen")
        self.lineEdit_pxlen.setEnabled(True)
        self.lineEdit_pxlen.setGeometry(QRect(180, 70, 41, 23))
        self.lineEdit_pxlen.setStyleSheet(u"border: 10px;\n"
"border-radius: 0px;\n"
"border-color: black;\n"
"background-color: rgba(120,120,120,50);\n"
"color:rgb(220,220,220);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.lineEdit_pxlen.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_26 = QLabel(self.page_3)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(230, 70, 161, 21))
        self.label_26.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.label_26.setWordWrap(False)
        self.lineEdit_imgnumber = QLineEdit(self.page_3)
        self.lineEdit_imgnumber.setObjectName(u"lineEdit_imgnumber")
        self.lineEdit_imgnumber.setEnabled(True)
        self.lineEdit_imgnumber.setGeometry(QRect(140, 130, 30, 23))
        self.lineEdit_imgnumber.setStyleSheet(u"border: 10px;\n"
"border-radius: 0px;\n"
"border-color: black;\n"
"background-color: rgba(120,120,120,50);\n"
"color:rgb(220,220,220);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_29 = QLabel(self.page_3)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(260, 70, 161, 21))
        self.label_29.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.label_29.setWordWrap(False)
        self.label_28 = QLabel(self.page_3)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(230, 10, 161, 21))
        self.label_28.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.label_28.setWordWrap(False)
        self.label_22 = QLabel(self.page_3)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(25, 100, 191, 21))
        self.label_22.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.label_22.setWordWrap(False)
        self.pushButton_browse = QPushButton(self.page_3)
        self.pushButton_browse.setObjectName(u"pushButton_browse")
        self.pushButton_browse.setGeometry(QRect(25, 160, 91, 23))
        self.pushButton_browse.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	background-color: rgb(90, 90, 90);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(155, 0, 0);\n"
"	color: white;\n"
"}")
        self.checkBox_autoaddimgnumber = QCheckBox(self.page_3)
        self.checkBox_autoaddimgnumber.setObjectName(u"checkBox_autoaddimgnumber")
        self.checkBox_autoaddimgnumber.setGeometry(QRect(260, 133, 151, 17))
        self.checkBox_autoaddimgnumber.setStyleSheet(u"QCheckBox {\n"
"	\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: none;\n"
"	color: rgb(220,220,220);\n"
"}")
        self.checkBox_autoaddimgnumber.setChecked(True)
        self.pushButton_loadsettings = QPushButton(self.page_3)
        self.pushButton_loadsettings.setObjectName(u"pushButton_loadsettings")
        self.pushButton_loadsettings.setGeometry(QRect(10, 200, 200, 23))
        self.pushButton_loadsettings.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	background-color: rgb(90, 90, 90);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(155, 0, 0);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 0, 0);\n"
"	color: white;\n"
"}")
        self.pushButton_loadsettings.setCheckable(False)
        self.pushButton_savesettings = QPushButton(self.page_3)
        self.pushButton_savesettings.setObjectName(u"pushButton_savesettings")
        self.pushButton_savesettings.setGeometry(QRect(230, 200, 200, 23))
        self.pushButton_savesettings.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	background-color: rgb(120,0,0);\n"
"	color: white;\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 0, 0);\n"
"	color: white;\n"
"}\n"
"\n"
"")
        self.pushButton_savesettings.setCheckable(False)
        self.label_38 = QLabel(self.page_3)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(25, 70, 161, 21))
        self.label_38.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.label_38.setWordWrap(False)
        self.lineEdit_Ttimelaps = QLineEdit(self.page_3)
        self.lineEdit_Ttimelaps.setObjectName(u"lineEdit_Ttimelaps")
        self.lineEdit_Ttimelaps.setEnabled(True)
        self.lineEdit_Ttimelaps.setGeometry(QRect(180, 40, 41, 23))
        self.lineEdit_Ttimelaps.setStyleSheet(u"border: 10px;\n"
"border-radius: 0px;\n"
"border-color: black;\n"
"background-color: rgba(120,120,120,50);\n"
"color:rgb(220,220,220);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.lineEdit_Ttimelaps.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_39 = QLabel(self.page_3)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(230, 40, 191, 21))
        self.label_39.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.label_39.setWordWrap(False)
        self.checkBox_timelapse = QCheckBox(self.page_3)
        self.checkBox_timelapse.setObjectName(u"checkBox_timelapse")
        self.checkBox_timelapse.setGeometry(QRect(260, 43, 151, 17))
        self.checkBox_timelapse.setStyleSheet(u"QCheckBox {\n"
"	\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: none;\n"
"	color: rgb(220,220,220);\n"
"}")
        self.checkBox_timelapse.setChecked(False)
        self.stackedWidget_settings.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.label_24 = QLabel(self.page_4)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(20, 75, 71, 21))
        self.label_24.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.label_30 = QLabel(self.page_4)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(20, 45, 81, 21))
        self.label_30.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.horizontalSlider_lightness = QSlider(self.page_4)
        self.horizontalSlider_lightness.setObjectName(u"horizontalSlider_lightness")
        self.horizontalSlider_lightness.setGeometry(QRect(99, 75, 291, 22))
        self.horizontalSlider_lightness.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: 1px solid black;\n"
"    height: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"    margin: 2px 0;\n"
"	background: rgba(100, 150, 200,50);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: rgb(100,150,200);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 18px;\n"
"    margin: -2px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"    border-radius: 3px;\n"
"}")
        self.horizontalSlider_lightness.setMinimum(0)
        self.horizontalSlider_lightness.setMaximum(100)
        self.horizontalSlider_lightness.setValue(25)
        self.horizontalSlider_lightness.setOrientation(Qt.Horizontal)
        self.horizontalSlider_lightness.setInvertedAppearance(False)
        self.horizontalSlider_saturation = QSlider(self.page_4)
        self.horizontalSlider_saturation.setObjectName(u"horizontalSlider_saturation")
        self.horizontalSlider_saturation.setGeometry(QRect(99, 45, 291, 22))
        self.horizontalSlider_saturation.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: 1px solid black;\n"
"    height: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"    margin: 2px 0;\n"
"	background: rgba(100, 150, 200,50);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: rgb(100,150,200);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 18px;\n"
"    margin: -2px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"    border-radius: 3px;\n"
"}")
        self.horizontalSlider_saturation.setMinimum(0)
        self.horizontalSlider_saturation.setMaximum(100)
        self.horizontalSlider_saturation.setValue(50)
        self.horizontalSlider_saturation.setOrientation(Qt.Horizontal)
        self.horizontalSlider_saturation.setInvertedAppearance(False)
        self.label_31 = QLabel(self.page_4)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(20, 110, 261, 21))
        self.label_31.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.horizontalSlider_contrastgrid = QSlider(self.page_4)
        self.horizontalSlider_contrastgrid.setObjectName(u"horizontalSlider_contrastgrid")
        self.horizontalSlider_contrastgrid.setGeometry(QRect(99, 170, 291, 22))
        self.horizontalSlider_contrastgrid.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: 1px solid black;\n"
"    height: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"    margin: 2px 0;\n"
"	background: rgba(100, 150, 200,50);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: rgb(100,150,200);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 18px;\n"
"    margin: -2px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"    border-radius: 3px;\n"
"}")
        self.horizontalSlider_contrastgrid.setMinimum(1)
        self.horizontalSlider_contrastgrid.setMaximum(50)
        self.horizontalSlider_contrastgrid.setValue(8)
        self.horizontalSlider_contrastgrid.setSliderPosition(8)
        self.horizontalSlider_contrastgrid.setOrientation(Qt.Horizontal)
        self.horizontalSlider_contrastgrid.setInvertedAppearance(False)
        self.horizontalSlider_contrastgrid.setInvertedControls(False)
        self.label_lightness = QLabel(self.page_4)
        self.label_lightness.setObjectName(u"label_lightness")
        self.label_lightness.setGeometry(QRect(392, 75, 31, 21))
        self.label_lightness.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(0, 0, 0, 50);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"color: rgb(220,220,220);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_lightness.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_saturation = QLabel(self.page_4)
        self.label_saturation.setObjectName(u"label_saturation")
        self.label_saturation.setGeometry(QRect(392, 45, 31, 21))
        self.label_saturation.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(0, 0, 0, 50);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"color: rgb(220,220,220);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_saturation.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_contrast = QLabel(self.page_4)
        self.label_contrast.setObjectName(u"label_contrast")
        self.label_contrast.setGeometry(QRect(382, 140, 31, 21))
        self.label_contrast.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(0, 0, 0, 50);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"color: rgb(220,220,220);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_contrast.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.checkBox_invert = QCheckBox(self.page_4)
        self.checkBox_invert.setObjectName(u"checkBox_invert")
        self.checkBox_invert.setGeometry(QRect(331, 200, 80, 31))
        self.checkBox_invert.setStyleSheet(u"QCheckBox {\n"
"	\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: none;\n"
"color: rgb(220,220,220);\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"}")
        self.checkBox_autostretch = QCheckBox(self.page_4)
        self.checkBox_autostretch.setObjectName(u"checkBox_autostretch")
        self.checkBox_autostretch.setGeometry(QRect(231, 200, 91, 31))
        self.checkBox_autostretch.setStyleSheet(u"QCheckBox {\n"
"	\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: none;\n"
"color: rgb(220,220,220);\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"}")
        self.checkBox_offsetsub = QCheckBox(self.page_4)
        self.checkBox_offsetsub.setObjectName(u"checkBox_offsetsub")
        self.checkBox_offsetsub.setGeometry(QRect(131, 200, 91, 31))
        self.checkBox_offsetsub.setStyleSheet(u"QCheckBox {\n"
"	\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: none;\n"
"color: rgb(220,220,220);\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"}")
        self.horizontalSlider_contrastamp = QSlider(self.page_4)
        self.horizontalSlider_contrastamp.setObjectName(u"horizontalSlider_contrastamp")
        self.horizontalSlider_contrastamp.setGeometry(QRect(99, 140, 291, 22))
        self.horizontalSlider_contrastamp.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: 1px solid black;\n"
"    height: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"    margin: 2px 0;\n"
"	background: rgba(100, 150, 200,50);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: rgb(100,150,200);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 18px;\n"
"    margin: -2px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"    border-radius: 3px;\n"
"}")
        self.horizontalSlider_contrastamp.setMinimum(1)
        self.horizontalSlider_contrastamp.setMaximum(100)
        self.horizontalSlider_contrastamp.setValue(20)
        self.horizontalSlider_contrastamp.setSliderPosition(20)
        self.horizontalSlider_contrastamp.setOrientation(Qt.Horizontal)
        self.horizontalSlider_contrastamp.setInvertedAppearance(False)
        self.horizontalSlider_contrastamp.setInvertedControls(False)
        self.label_contrast_2 = QLabel(self.page_4)
        self.label_contrast_2.setObjectName(u"label_contrast_2")
        self.label_contrast_2.setGeometry(QRect(392, 170, 21, 21))
        self.label_contrast_2.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(0, 0, 0, 50);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"color: rgb(220,220,220);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_contrast_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_32 = QLabel(self.page_4)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(20, 170, 81, 21))
        self.label_32.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.label_33 = QLabel(self.page_4)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(20, 140, 81, 21))
        self.label_33.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.checkBox_ace = QCheckBox(self.page_4)
        self.checkBox_ace.setObjectName(u"checkBox_ace")
        self.checkBox_ace.setGeometry(QRect(31, 200, 80, 31))
        self.checkBox_ace.setStyleSheet(u"QCheckBox {\n"
"	\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: none;\n"
"color: rgb(220,220,220);\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"}")
        self.frame_8 = QFrame(self.page_4)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(10, 5, 421, 31))
        self.frame_8.setStyleSheet(u"border-radius: 0px;\n"
"border: 3px solid rgba(0, 0, 0, 30);\n"
"background-color: rgba(0, 0, 0, 30);\n"
"\n"
"")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.checkBox_applyimageman = QCheckBox(self.frame_8)
        self.checkBox_applyimageman.setObjectName(u"checkBox_applyimageman")
        self.checkBox_applyimageman.setGeometry(QRect(50, 0, 331, 31))
        self.checkBox_applyimageman.setStyleSheet(u"QCheckBox {\n"
"	\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: none;\n"
"	color: rgb(220,0,0);\n"
"	\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"}")
        self.label_34 = QLabel(self.page_4)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(417, 141, 21, 21))
        self.label_34.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.label_35 = QLabel(self.page_4)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(417, 170, 21, 21))
        self.label_35.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.stackedWidget_settings.addWidget(self.page_4)
        self.pushButton_exit = QPushButton(camcom_mainwin)
        self.pushButton_exit.setObjectName(u"pushButton_exit")
        self.pushButton_exit.setGeometry(QRect(410, 20, 20, 20))
        self.pushButton_exit.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	background-color: rgb(120,0,0);\n"
"	background-image: url(:/icons/exit.png);\n"
"	color: white;\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 0, 0);\n"
"	color: white;\n"
"}\n"
"\n"
"")

        self.retranslateUi(camcom_mainwin)

        self.stackedWidget_scopetype.setCurrentIndex(2)
        self.stackedWidget_settings.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(camcom_mainwin)
    # setupUi

    def retranslateUi(self, camcom_mainwin):
        camcom_mainwin.setWindowTitle(QCoreApplication.translate("camcom_mainwin", u"Form", None))
        self.label.setText(QCoreApplication.translate("camcom_mainwin", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#f0f0f0;\">ScopeControl</span></p></body></html>", None))
        self.pushButton_comrefresh.setText(QCoreApplication.translate("camcom_mainwin", u"refresh", None))
        self.pushButton_comconnect.setText(QCoreApplication.translate("camcom_mainwin", u"connect", None))
        self.label_4.setText(QCoreApplication.translate("camcom_mainwin", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; font-style:italic; color:#6496c8;\">camera</span></p></body></html>", None))
        self.pushButton_screenmode.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_settings.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushButton_settings.setText("")
        self.pushButton_measure.setText("")
        self.pushButton_saveimg.setText("")
        self.pushButton_record.setText("")
        self.pushButton_freeze.setText("")
        self.pushButton_average.setText("")
        self.label_19.setText(QCoreApplication.translate("camcom_mainwin", u"<html><head/><body><p align=\"right\"><span style=\" color:#ffffff;\">Settings</span></p></body></html>", None))
        self.pushButton_imagepara.setText("")
        self.checkBox_imginfo.setText(QCoreApplication.translate("camcom_mainwin", u"show info", None))
        self.checkBox_flipx.setText(QCoreApplication.translate("camcom_mainwin", u"flip x-axis", None))
        self.label_aver.setText(QCoreApplication.translate("camcom_mainwin", u"0", None))
        self.label_15.setText(QCoreApplication.translate("camcom_mainwin", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#dcdcdc;\">Brightness</span></p></body></html>", None))
        self.label_bright.setText(QCoreApplication.translate("camcom_mainwin", u"50", None))
        self.checkBox_flipy.setText(QCoreApplication.translate("camcom_mainwin", u"flip y-axis", None))
        self.label_14.setText(QCoreApplication.translate("camcom_mainwin", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#dcdcdc;\">Exposure</span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("camcom_mainwin", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#dcdcdc;\">Gain</span></p></body></html>", None))
        self.checkBox_grayscale.setText(QCoreApplication.translate("camcom_mainwin", u"grayscale", None))
        self.label_exposure.setText(QCoreApplication.translate("camcom_mainwin", u"-10", None))
        self.label_status.setText(QCoreApplication.translate("camcom_mainwin", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ff0000;\">waiting</span></p></body></html>", None))
        self.pushButton_mini.setText("")
        self.label_17.setText(QCoreApplication.translate("camcom_mainwin", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#dcdcdc;\">Intensity</span></p></body></html>", None))
        self.label_bright_2.setText(QCoreApplication.translate("camcom_mainwin", u"100", None))
        self.label_18.setText(QCoreApplication.translate("camcom_mainwin", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#dcdcdc;\">Illumination mode:</span></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("camcom_mainwin", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#dcdcdc;\">Microscope Objective:</span></p></body></html>", None))
        self.pushButton_lampconnect.setText(QCoreApplication.translate("camcom_mainwin", u"connect", None))
        self.label_5.setText(QCoreApplication.translate("camcom_mainwin", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; font-style:italic; color:#6496c8;\">lamp</span></p></body></html>", None))
        self.pushButton_lamprefresh.setText(QCoreApplication.translate("camcom_mainwin", u"refresh", None))
        self.label_21.setText(QCoreApplication.translate("camcom_mainwin", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#dcdcdc;\">Telescope type:</span></p></body></html>", None))
        self.pushButton_mountconnect.setText(QCoreApplication.translate("camcom_mainwin", u"connect", None))
        self.label_6.setText(QCoreApplication.translate("camcom_mainwin", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; font-style:italic; color:#6496c8;\">mount</span></p></body></html>", None))
        self.pushButton_mountrefresh.setText(QCoreApplication.translate("camcom_mainwin", u"refresh", None))
        self.pushButton_freeze_2.setText("")
        self.pushButton_freeze_3.setText("")
        self.pushButton_freeze_4.setText("")
        self.pushButton_freeze_5.setText("")
        self.checkBox_tracking.setText(QCoreApplication.translate("camcom_mainwin", u"activate tracking (counter rotation of earth)", None))
        self.label_37.setText(QCoreApplication.translate("camcom_mainwin", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#dcdcdc;\">Mount speed</span></p></body></html>", None))
        self.label_mountspeed.setText(QCoreApplication.translate("camcom_mainwin", u"0", None))
        self.label_36.setText(QCoreApplication.translate("camcom_mainwin", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">ScopeControl - PrintedLabs</span></p><p align=\"justify\"><span style=\" font-size:10pt; font-weight:600; color:#dcdcdc;\">Version: 1.2 - 07/25/2023</span></p><p align=\"justify\"><span style=\" font-size:10pt; font-weight:600; color:#dcdcdc;\">Would you like to learn more about ScopeControl and get<br/>a tutorial on all implemented functions. You can find this and<br/>much more on our website </span><a href=\"www.printedlabs.uni-bayreuth.de\"><span style=\" font-size:10pt; font-weight:600; text-decoration: underline; color:#dc0000;\">www.printedlabs.uni-bayreuth.de</span></a><span style=\" font-size:10pt; font-weight:600; color:#dcdcdc;\">!</span></p></body></html>", None))
        self.pushButton_micmode.setText(QCoreApplication.translate("camcom_mainwin", u"Microscope", None))
        self.pushButton_telmode.setText(QCoreApplication.translate("camcom_mainwin", u"Telescope", None))
        self.pushButton_infobox.setText("")
        self.lineEdit_imgformat.setText(QCoreApplication.translate("camcom_mainwin", u"bmp", None))
        self.label_25.setText(QCoreApplication.translate("camcom_mainwin", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#dcdcdc;\">timelapse frame-period:</span></p></body></html>", None))
        self.label_23.setText(QCoreApplication.translate("camcom_mainwin", u"<html><head/><body><p><span style=\" font-size:12pt; color:#dcdcdc;\">.</span></p></body></html>", None))
        self.lineEdit_frameavnum.setText(QCoreApplication.translate("camcom_mainwin", u"20", None))
        self.lineEdit_filename.setText(QCoreApplication.translate("camcom_mainwin", u"data", None))
        self.lineEdit_filepath.setText(QCoreApplication.translate("camcom_mainwin", u"C:\\", None))
        self.label_27.setText(QCoreApplication.translate("camcom_mainwin", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#dcdcdc;\">Frame averaging:</span></p></body></html>", None))
        self.lineEdit_pxlen.setText(QCoreApplication.translate("camcom_mainwin", u"2.2", None))
        self.label_26.setText(QCoreApplication.translate("camcom_mainwin", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#dcdcdc;\">\u00b5m</span></p></body></html>", None))
        self.lineEdit_imgnumber.setText(QCoreApplication.translate("camcom_mainwin", u"1", None))
        self.label_29.setText(QCoreApplication.translate("camcom_mainwin", u"<html><head/><body><p><span style=\" font-size:10pt; color:#dcdcdc;\">(quadratic pixels)</span></p></body></html>", None))
        self.label_28.setText(QCoreApplication.translate("camcom_mainwin", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#dcdcdc;\">frames </span><span style=\" font-size:10pt; color:#dcdcdc;\">(to average)</span></p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("camcom_mainwin", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#dcdcdc;\">Image filenames and folder:</span></p></body></html>", None))
        self.pushButton_browse.setText(QCoreApplication.translate("camcom_mainwin", u"browse", None))
        self.checkBox_autoaddimgnumber.setText(QCoreApplication.translate("camcom_mainwin", u"autoadd image numbers", None))
        self.pushButton_loadsettings.setText(QCoreApplication.translate("camcom_mainwin", u"load settings", None))
        self.pushButton_savesettings.setText(QCoreApplication.translate("camcom_mainwin", u"save settings", None))
        self.label_38.setText(QCoreApplication.translate("camcom_mainwin", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#dcdcdc;\">Camera pixel length:</span></p></body></html>", None))
        self.lineEdit_Ttimelaps.setText(QCoreApplication.translate("camcom_mainwin", u"1", None))
        self.label_39.setText(QCoreApplication.translate("camcom_mainwin", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#dcdcdc;\">s</span></p></body></html>", None))
        self.checkBox_timelapse.setText(QCoreApplication.translate("camcom_mainwin", u"activate timelapse", None))
        self.label_24.setText(QCoreApplication.translate("camcom_mainwin", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#dcdcdc;\">Lightness</span></p></body></html>", None))
        self.label_30.setText(QCoreApplication.translate("camcom_mainwin", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#dcdcdc;\">Saturation</span></p></body></html>", None))
        self.label_31.setText(QCoreApplication.translate("camcom_mainwin", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#dcdcdc;\">Adaptive contrast enhancement (HDR)</span></p></body></html>", None))
        self.label_lightness.setText(QCoreApplication.translate("camcom_mainwin", u"1.00", None))
        self.label_saturation.setText(QCoreApplication.translate("camcom_mainwin", u"50", None))
        self.label_contrast.setText(QCoreApplication.translate("camcom_mainwin", u"100", None))
        self.checkBox_invert.setText(QCoreApplication.translate("camcom_mainwin", u"invert image", None))
        self.checkBox_autostretch.setText(QCoreApplication.translate("camcom_mainwin", u"autostretch", None))
        self.checkBox_offsetsub.setText(QCoreApplication.translate("camcom_mainwin", u"offset corr.", None))
        self.label_contrast_2.setText(QCoreApplication.translate("camcom_mainwin", u"50", None))
        self.label_32.setText(QCoreApplication.translate("camcom_mainwin", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#dcdcdc;\">GridSize</span></p></body></html>", None))
        self.label_33.setText(QCoreApplication.translate("camcom_mainwin", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#dcdcdc;\">Amplitude</span></p></body></html>", None))
        self.checkBox_ace.setText(QCoreApplication.translate("camcom_mainwin", u"activate HDR", None))
        self.checkBox_applyimageman.setText(QCoreApplication.translate("camcom_mainwin", u"apply image processing (higher computational effort)", None))
        self.label_34.setText(QCoreApplication.translate("camcom_mainwin", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#dcdcdc;\">%</span></p></body></html>", None))
        self.label_35.setText(QCoreApplication.translate("camcom_mainwin", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#dcdcdc;\">px</span></p></body></html>", None))
        self.pushButton_exit.setText("")
    # retranslateUi

