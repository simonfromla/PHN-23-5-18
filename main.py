from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup
import urllib.request

# Firefox
driver = webdriver.Firefox()
# driver.get("http:google.com")

# If exception:
# Webdriver needs location of chromedriver and browser
# options = webdriver.ChromeOptions()
# options.binary_location = "/Applications/GoogleChrome.app/Contents/MacOS/Google Chrome"
# chromedriver = "/Users/sjung/Downloads/chromedriver"
# driver = webdriver.Chrome(chromedriver, chrome_options=options)
# driver.get("http:google.com")
def build_url(search_start_date, search_end_date, genre=None):
    url = f'https://www.bandsintown.com/c/seoul-korea-republic-of?came_from=253&date={search_start_date}T14%3A00%3A00%2C{search_end_date}T02%3A00%3A00&date_filter=Next+Week&genre_filter={genre}'
    return url

url = build_url('2018-05-23', '2018-06-12')
driver.get(url)


"""TO-DO

Build a genre dict
Turn into a CLI app (sys.argv)
Make modular (define Class)

"""
# genres = {
#     'R&B/Soul': 'R%26B%2FSoul',
#     'Hip Hop': 'Hip+Hop'
# }
