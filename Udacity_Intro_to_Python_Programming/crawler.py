from bs4 import BeautifulSoup
import requests


def get_valid_wiki_link(links):
    for link in links:
        cur_href = link.get('href')
        if (cur_href and "/wiki/" in cur_href) and (not "File:" in cur_href) and (not "disambiguation" in cur_href) :
             break
    return cur_href

def print_all_links(links):
    for link in links:
        print("link is :\n")
        print(link);


def loop_found(curlink, articles):
    for link in articles:
        if link == curlink:
            return True
    return False


def is_traversal_end_reached(curlink,articles):
    is_loop = loop_found(curlink,articles)
    return is_loop

response = requests.get("https://en.wikipedia.org/wiki/Special:Random")
# response = requests.get("https://en.wikipedia.org/wiki/Indus_Valley_Civilisation")

soup = BeautifulSoup(response.text,'html.parser')
is_loop_found = False
is_philosophy_found = False
article_chain = []
http_wiki = "https://wikipedia.org"

while not is_loop_found or not is_philosophy_found:
    links = soup.body.find_all("a")
    # print_all_links(links)
    curlink = get_valid_wiki_link(links)
    print("curlink is:" + str(curlink))
    article_chain.append(curlink)
    chain_len = len(article_chain)
    curURL = http_wiki+curlink
    cur_response = requests.get(curURL)
    soup = BeautifulSoup(cur_response.text,'html.parser')
    # print(article_chain)
    links = soup.body.find_all("a")
    curlink = get_valid_wiki_link(links)
    if is_traversal_end_reached(curlink,article_chain):
        break
print(article_chain)


