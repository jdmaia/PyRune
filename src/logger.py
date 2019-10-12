import time
from datetime import datetime

class Logger:
    fstr  = ''
    fname = ''
    fmode  = ''
    tstamp = ''
    def __init__(self, name, mode):
        self.fname = name
        self.fmode = mode
        self.fstr  = open(self.fname, self.fmode)
        print("Starting logger for " + self.fname)

    def Log(self, append):
        print(self.getStamp()+append, file = self.fstr)

    def getStamp(self):
        return "[" + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "]: "
