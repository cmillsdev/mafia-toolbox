import requests
from time import sleep
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

    for page in range(1, last_page+1):
        print(f"Scraping page {page} of {last_page}...")
        posts.append(scrape_page(url + page_params + str(page)))
        sleep(0.25)

    return posts


def scrape_page(url):
    soup = bs(requests.get(url, cookies=SA_COOKIE, timeout=5).content, "html.parser")
    posts = soup.find(id='thread').find_all('table')
    page = []
    
    for post in posts:
        username = post.find("dt", class_="author").text.strip()
        timestamp = " ".join(post.find("td", class_="postdate").get_text(strip=True).replace("#?","").split())
        post = post.find('td', class_='postbody')
        page.append({
            "username": username,
            "timestamp": timestamp,
            "post": post.text.strip()
        })

    return page


