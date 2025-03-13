import requests
from bs4 import BeautifulSoup as bs
from config import SA_COOKIE

def get_last_page(soup):
    select_elem = soup.find('select')
    option_elems = select_elem.find_all('option')
    return len(option_elems)

def scrape_thread(url):
    soup = bs(requests.get(url, cookies=SA_COOKIE, timeout=5).content, 'html.parser')
    last_page = get_last_page(soup)
    page_params = "&pagenumber="
    posts = []

    for page in range(1, last_page):
        pass

def scrape_page(url):
    soup = bs(requests.get(url, cookies=SA_COOKIE, timeout=5).content, "html.parser")
    posts = soup.find(id='thread').find_all('table')
    print(posts)


