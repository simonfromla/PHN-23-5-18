from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup
import urllib.request

# Firefox
# driver = webdriver.Firefox()
# driver.get("http:google.com")

# If exception, Webdriver needs location of chromedriver and browser
options = webdriver.ChromeOptions()
options.binary_location = "/Applications/GoogleChrome.app/Contents/MacOS/Google Chrome"
chromedriver = "/Users/sjung/Downloads/chromedriver"
driver = webdriver.Chrome(chromedriver, chrome_options=options)
# driver.get("http:google.com")


def build_url(search_start_date, search_end_date, genre=None):
    url = f'https://www.bandsintown.com/c/seoul-korea-republic-of?came_from=253&date={search_start_date}T14%3A00%3A00%2C{search_end_date}T02%3A00%3A00&date_filter=Next+Week&genre_filter={genre}'
    return url


def load_page(url):
    driver.get(url)
    delay = 1
    # making sure the elements that we're after are loaded
    # don't want to extract elements before the page has loaded
    try:
        wait = WebDriverWait(driver, delay)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME,
                                                   "index-a51e56ea"))) # CSS_SELECTOR
        print("Page is ready")
    except TimeoutException:
        print("Loading took too muc time!")


def get_event_artist():
    events = driver.find_elements_by_class_name("event-9d0dee19")
    event_list = [e.text for e in events]
    # for event in events:
    #     print(event.text)
    print("event list: ", event_list)


def get_event_date(url):
    event_dates = []
    html = urllib.request.urlopen(url)
    # soup = BeautifulSoup(html, "lxml")
    soup = BeautifulSoup(html, "html.parser")
    # soup = BeautifulSoup(html)
    for date in soup.findAll("h2", {"class": "event-9d0dee19"}):
        print(date.findNext('div').contents)
        event_dates.append(date.findNext('div').contents)
    return event_dates


def quit_browser():
    driver.close()


url = build_url('2018-05-23', '2018-06-12')
load_page(url)
# get_event_artist()
get_event_date(url)
# driver.get(url)
quit_browser()

"""TO-DO

Build a genre dict
Turn into a CLI app (sys.argv)
Make modular (define Class)

"""
# genres = {
#     'R&B/Soul': 'R%26B%2FSoul',
#     'Hip Hop': 'Hip+Hop'
# }
