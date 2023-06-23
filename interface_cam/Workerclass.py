import PySide6.QtCore as qtc
from time import sleep as sleep

class CamreadWorker(qtc.QRunnable):
    
    def __init__(self, *args, **kwargs):
        super(CamreadWorker, self).__init__()
        self.parentwin = args[0]
    
    def run(self):
        self.parentwin.camreadupdate()
        
class Lampconnect(qtc.QRunnable):
    def __init__(self, *args, **kwargs):
        super(Lampconnect, self).__init__()
        self.parentwin = args[0]
    
    def run(self):
        self.parentwin.connect2com()


class Camconnect(qtc.QRunnable):
    def __init__(self, *args, **kwargs):
        super(Camconnect, self).__init__()
        self.parentwin = args[0]
    
    def run(self):
        self.parentwin.connect2cam()

