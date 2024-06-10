from urllib.request import Request, urlopen
from bs4 import BeautifulSoup # type: ignore
import re


def openlink(site):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    req = Request(site, headers=headers)
    html = urlopen(req)
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def scrapingData(soup):

    scorecard_list = []
    class_tag = soup.find('main', {'class': 'main'})
    scorecards = class_tag.find_all('h3')
    for i in scorecards:
        scorecard_list.append(i.text) 
    return scorecard_list

def regular_expression(scorecard_list):

    cleaning = list(filter(lambda x: re.search(r'scorecard', x, re.IGNORECASE), scorecard_list))
    container = tuple(cleaning)
    return container

def main():
    site = 'https://www.cornucopia.org/scorecards/'
    soup = openlink(site)
    scorecard_list = scrapingData(soup)
    container = regular_expression(scorecard_list)
    print(container)
main()


