# Tor Web Scraper
# python modules
import sys
# our modules
from modules.scrapeURL import scrapeURL
from modules.txtFileHandler import TXTHandler
from modules.csvFileHandler import CSVHandler

# current supported modes and their correspoding functions
MODES = {
    "csv":CSVHandler,
    "txt":TXTHandler,
    "url":scrapeURL, #if it is url then the url is given directly
}
USAGEMESSAGE = "USAGE: \"python scraper.py mode args...\"\nsupported modes:\n\tcsv\n\ttxt\n\turl"

# main coordinates the program
def main(args):
    # validate args
    if len(args) < 3:
        print(USAGEMESSAGE)
        return 0;
    # check that the mode is recognised
    mode = args[1]
    if not (mode in MODES.keys()):
        print(USAGEMESSAGE)
        return 0;
    # check if tor is running:
    # RUN TOR 
    #app = Application(backend="win32").start(r"./Tor Browser/Browser/firefox.exe")
    #sleep(1) # give tor a second to launch
    # run the relevant mode's function
    MODES[f"{mode}"](args[2])
    # CLOSE TOR
    #os.system("TASKKILL /F /IM firefox.exe") # app does not kill so I use this nuclear option
    #app.kill() #This does not work for some reason

if __name__ == "__main__":
    main(sys.argv)
