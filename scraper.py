# Tor Web Scraper
import sys
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
    if len(args) < 3:
        print(USAGEMESSAGE)
        return 0;
    mode = args[1]
    if not (mode in MODES.keys()):
        print(USAGEMESSAGE)
        return 0;
    # run the relevant mode's function
    MODES[f"{mode}"](args[2])

if __name__ == "__main__":
    main(sys.argv)
