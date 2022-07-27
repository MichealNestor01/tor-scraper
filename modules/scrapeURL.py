# scrapeURL.py
# this is the main function that orchestrates the webscraping
from modules.getDriver import getDriver
from modules.scrapeData import scrapeData
from modules.returnCodes import *


# This function actually performes the webscraping of a url
def scrapeURL(url, showoutput=True):
    driver = getDriver()
    try:
        driver.get(url)
    except:
        print(f"ERROR: UNABLE TO REACH {url}")
        return URL_ERROR
    pageTitle = scrapeData(driver.page_source)
    # save a screenshot from the website
    driver.save_full_page_screenshot(f"./screenshots/{pageTitle}" + ".png")
    driver.quit()
    if showoutput:
        print(f"Scraped: {pageTitle}\n\tSource code saved to ./htmldata/{pageTitle}.html\n\tScreenshot saved to ./screenshots/{pageTitle}.png")
    return NO_ERROR
