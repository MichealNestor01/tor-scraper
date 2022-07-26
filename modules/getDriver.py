#   getDriver.py 
#   This file returns the selenium web driver needed to for scraping. 
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

def getDriver():
    # headless ensures that the tor gui is not launched
    options = Options()
    options.headless = True
    
    # These files are needed for the selenium setup, if you have chosen to not have tor installed in the local directory,
    # you can change these paths, the binary and profile may be in a different place on unix based systems.
    binary = FirefoxBinary(r"./Tor Browser/Browser/firefox.exe")
    profile = FirefoxProfile(r"./Tor Browser/Browser/TorBrowser/Data/Browser/profile.default")
    return webdriver.Firefox(profile, binary, options=options)