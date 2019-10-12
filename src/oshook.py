from .osdetector import OSDetector
from pynput.keyboard import Key, Controller
import time

class OSHook:
    osdet = 0
    pid   = 0
    kb    = 0
    time  = 0

    def __init__(self, time, key):
        self.osdet = OSDetector()
        self.kb  = Controller()
        self.time = time
        self.htk  = key

    def preshtk(self):
        while(true):
            self.kb.press(self.key)
            self.kb.release(self.key)
            sleep(self.time) # presses the keys then sleeps

    def test(self):
        print("Will try to send commands to a given process")
        print("Sleeping for 10 seconds, please select the process quick")
        time.sleep(5)
        self.kb.type('test')
        # this is not working apparently?
