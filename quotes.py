import argparse
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import csv
import os

def geturl(tag):
    return f'https://www.goodreads.com/quotes/tag/{tag}'


def get_soup(url):
    response = urlopen(Request(url))
    return BeautifulSoup(response, 'html.parser')

def extract_quotes_elements_from_soup(soup):
    elements_quotes = soup.find_all("div", class_= "quote mediumText")
    return elements_quotes

def extractquote(soup):
    quotes= soup.find_all('div',class_="quoteText")
    # quote= soup.find('div',class_="quoteText").get_text("|", strip=True)
    # quote = quote.split('|')[0]
    # quote = re.sub('^“', '', quote)
    # quote = re.sub('”\s?$', '', quote)
    quotes_list=[]
    for q in quotes:
        quote = q.get_text("|", strip=True)
        quote = quote.split('|')[0]
        quote = re.sub('^“', '', quote)
        quote = re.sub('”\s?$', '', quote)
        quotes_list.append(quote)
    authors = soup.find_all('span', class_= 'authorOrTitle')
    author_list =[]
    for a in authors:
        author = a.get_text(strip=True)
        author = author.strip()
        author = author.rstrip(',')
        author_list.append(author)

    return {author_list[i]: quotes_list[i] for i in range(len(quotes_list))}


url = geturl("hero")
soup = get_soup(url)
quote_element = extract_quotes_elements_from_soup(soup)
print(type(quote_element))
print(type(soup))
x= extractquote(soup)

print(x)
