#   scrapeData.py 
#   This file returns the page title, and saves the sourcecode from a website 
import bs4
from modules.sanatiser import sanatiseTitle

# Takes the source code of a given site (driver.page_source)
def scrapeData(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    rawTitle = soup.title.string
    title = sanatiseTitle(rawTitle)
    with open(f"./htmldata/{title}", "w+", encoding="utf-8") as file:
        file.write(html)
    return title

