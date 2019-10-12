# NOTE: This class needs to be a thread (or run in a thread)
import threading # running stuff concurrently
import time # sleep()

class Rune:
    time     = 0
    manacost = 0
    thread   = 0
    abort    = 0
    hotkey   = ''
    kb       = ''
    name     = ''
    logger   = ''

    def __init__(self, name, kb, hotkey, time, manacost, logger):
        self.name     = name
        self.time     = time
        self.manacost = manacost
        self.hotkey   = hotkey
        self.kb       = kb  #KB is the hook for keyboards
        self.logger = logger
        self.thread   = threading.Thread(target=self.RunThread(), args=())
        self.abort    = False

    def RunThread(self):
        while (not(self.abort)):
            self.logger.Log("Brewing rune " + self.name + " (sleep time is " + str(self.time) + ")")
            self.kb.press(self.hotkey)
            self.kb.release(self.hotkey)
            time.sleep(self.atime)
        self.Abort()

    def Brew(self, logger):
        # starts thread
        self.logger = logger
        self.thread.start()
        # default thread keeps running whilst self.thread gets started
        return

    def Abort(Self):
        self.abort = True
        thread.join()
