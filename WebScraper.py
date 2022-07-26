# Tor Web Scraper
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import bs4
import sys


def scrape(url):
    options = Options()
    options.headless = True
    binary = FirefoxBinary(r"C:/Users/Student/Desktop/Tor Browser/Browser/firefox.exe")
    profile = FirefoxProfile(r"C:/Users/Student/Desktop/Tor Browser/Browser/TorBrowser/Data/Browser/profile.default")
    driver = webdriver.Firefox(profile, binary, options=options)

    driver.get(url)
    html = driver.page_source

    soup = bs4.BeautifulSoup(html, 'html.parser')
    title = soup.title.string
    print('Scraping:', title)

    try:
        with open(title, "w+", encoding="utf-8") as html_file:
            html_file.write(html)

        driver.save_full_page_screenshot(title + ".png")

    except OSError:
        title = title.split('|')[0]
        with open(title + ".html", "w+", encoding="utf-8") as html_file:
            html_file.write(html)

        driver.save_full_page_screenshot(title + ".png")

    driver.quit()


filename = 'web_addresses' #str(sys.argv[1])

with open(filename) as file:
    for url in file.readlines():
        scrape(url)