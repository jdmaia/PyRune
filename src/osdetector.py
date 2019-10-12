import os
import platform
class OSDetector:
  name = ''
  platform = ''
  type = ''
  release = ''

  def __init__(self):
    self.name   = os.name
    self.system = platform.system()
    self.release = platform.release()
    self.setType()
    # fill 'type' field later

  def getName(self):
    return self.name;

  def getSystem(self):
    return self.system;

  def getRelease(self):
    return self.release;

  def setType(self):
    if(self.system == "darwin"):
        self.type = 0
    elif(self.system == "linux"):
        self.type = 1
    elif(self.system == "windows"):
        self.type = 2

  def printSpecs(self):
    print("Running on "+ self.getName() + " " + self.getSystem() + " release: " + self.release)
