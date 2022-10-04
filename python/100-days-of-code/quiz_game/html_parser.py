from urllib.request import urlopen
from bs4 import BeautifulSoup

def parse_site(url):
    html = urlopen(url).read()
    soup = BeautifulSoup(html, features="html.parser")

    for script in soup(["script", "style"]):
        script.extract()

    return soup.get_text()
