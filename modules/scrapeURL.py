# scrapeURL.py
# this is the main function that orchestrates the webscraping
from modules.getDriver import getDriver
from modules.scrapeData import scrapeData


# This function actually performes the webscraping of a url
def scrapeURL(url, showoutput=True):
    driver = getDriver()
    driver.get(url)
    pageTitle = scrapeData(driver.page_source)
    # save a screenshot from the website
    driver.save_full_page_screenshot(f"./screenshots/{pageTitle}" + ".png")
    driver.quit()
    if showoutput:
        print(f"Scraping: {pageTitle}\n\tSource code saved to ./htmldata/{pageTitle}.html\n\tScreenshot saved to ./screenshots/{pageTitle}.png")
