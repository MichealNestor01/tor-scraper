# txtFileHandler.py
# this handles reading urls from txt files
from modules.scrapeURL import scrapeURL
from modules.returnCodes import *

def TXTHandler(file):
    try:
        with open(file) as file:
            for url in file.readlines():
                returnCode = scrapeURL(url)
                if returnCode == WEBDRIVER_ERROR:
                    return WEBDRIVER_ERROR
    except FileNotFoundError:
        print(f"ERROR: {file} NOT FOUND")