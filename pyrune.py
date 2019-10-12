# simple python script to hook rune times in tibia
from src.osdetector import OSDetector
from src.oshook import OSHook
from src.rune   import Rune
from src.brewer import Brewer
from src.logger import Logger

from pynput.keyboard import Key, Controller

def main():
    print("__________")
    print("\______   \___.__._______ __ __  ____   ____")
    print("|     ___<   |  |\_  __ \  |  \/    \_/ __ \ ")
    print("|    |    \___  | |  | \/  |  /   |  \  ___/")
    print("|____|    / ____| |__|  |____/|___|  /\___  >")
    print("          \/                       \/     \/")
    logger = Logger("anubaiadu.log", "a")
    os = OSDetector()
    os.printSpecs()
    brewer = Brewer("anubaiadu", 100, logger)
    input =  Controller()
    rune = Rune("test", input, 'a', 10, 10, logger)
    brewer.AttachRune(rune)
    brewer.StartBrews()
    sleep(60)
    brewer.StopBrews()
    print("Cya!")
    # hook = OSHook()
    # hook.test()

if __name__ == '__main__':
    main();
