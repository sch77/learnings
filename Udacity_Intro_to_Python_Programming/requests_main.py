from bs4 import BeautifulSoup
import requests
import re


def print_all_links(links):
    for link in links:
        print("link is :\n")
        print(link.get('href'));

def get_valid_wiki_link(links):
    for link in links:
        cur_href = link.get('href')
        if( cur_href and "/wiki/" in cur_href ):
           break
    return link


# r = requests.get('https://en.wikipedia.org/wiki/Special:Random')
r = requests.get('https://en.wikipedia.org/wiki/Lincolnshire_derby')

soup = BeautifulSoup(r.text,"html.parser")
links = soup.body.find_all("a")
curlink = get_valid_wiki_link(links)
print(curlink)
# print_all_links(links)