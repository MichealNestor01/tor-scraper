# txtFileHandler.py
# this handles reading urls from txt files
from modules.scrapeURL import scrapeURL

def TXTHandler(file):
    try:
        with open(file) as file:
            for url in file.readlines():
                scrapeURL(url)
    except FileNotFoundError:
        print(f"ERROR: {file} NOT FOUND")