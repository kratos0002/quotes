import argparse
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import csv
import os
import requests
import time
import random
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


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


def url():
    tags = ['life', 'death', 'love', 'hate', 'america', 'kerouac', 'ontheroad', 'dharma', 'truth','harrypotter','batman', 'justice']
    number = random.randint(0,len(tags)-1)
    print(number)
    url = geturl(tags[number])
    soup = get_soup(url)
    quote_element = extract_quotes_elements_from_soup(soup)
    # print(type(quote_element))
    # print(type(soup))
    x= extractquote(soup)
    y=list(x.items())
    return y

<<<<<<< HEAD
def urlwitharg(arg):
    url = geturl(arg)
    soup = get_soup(url)
    quote_element = extract_quotes_elements_from_soup(soup)
    print(type(quote_element))
    print(type(soup))
    x= extractquote(soup)
    y=list(x.items())
    return y
=======
# def urlwitharg(arg):
#     url = geturl(arg)
#     soup = get_soup(url)
#     quote_element = extract_quotes_elements_from_soup(soup)
#     print(type(quote_element))
#     print(type(soup))
#     x= extractquote(soup)
#     y=list(x.items())
#     return y
>>>>>>> 3e0fb57f80371cd707c1c81ab8c4c5acb7035ac3



# for quote in y:
#     print(quote)
#     url = 'https://api.telegram.org/bot2024333055:AAHM_Pz9C8UOC316pMejalR6mWHcNfapa8o/sendMessage?chat_id=751449651&text="{}"'.format(quote)
#     requests.get(url)
#     # sends new quotes every 20seconds
#     time.sleep(300)


telegram_bot_token = "2024333055:AAHM_Pz9C8UOC316pMejalR6mWHcNfapa8o"
# updater = Updater(token=telegram_bot_token, use_context=True)
# dispatcher = updater.dispatcher


def random1(update, context):
    # fetch data from the api
    x = url()
<<<<<<< HEAD
    chat_ids = get_chat_id(update, context)
=======
>>>>>>> 3e0fb57f80371cd707c1c81ab8c4c5acb7035ac3
    number = random.randint(0, len(x)-1)
    quote=x[number]
    print(quote)
    # send message
<<<<<<< HEAD
    context.bot.send_message(chat_id=chat_ids, text=quote) 

def get_chat_id(update, context):
  chat_id = -1

  if update.message is not None:
    # from a text message
    chat_id = update.message.chat.id
  elif update.callback_query is not None:
    # from a callback message
    chat_id = update.callback_query.message.chat.id

    return chat_id

    

=======
    context.bot.send_message(chat_id=update.effective_chat.id, text=quote) 
>>>>>>> 3e0fb57f80371cd707c1c81ab8c4c5acb7035ac3

# def life(update, context):
#     # fetch data from the api
#     x = urlwitharg("life")
#     number = random.randint(1, len(x))
#     quote=x[number]
#     print(quote)
#     # send message
#     context.bot.send_message(chat_id=update.effective_chat.id, text=quote) 
# # quotes_handler = CommandHandler('random', random)
# # dispatcher.add_handler(quotes_handler)

<<<<<<< HEAD
# def error(update, context):
#     context.bot.send_message('an error occured')
=======
>>>>>>> 3e0fb57f80371cd707c1c81ab8c4c5acb7035ac3

def main():
    updater = Updater(telegram_bot_token)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('random',random1))
    # dp.add_handler(CommandHandler('life',life))
<<<<<<< HEAD
    # dp.add_handler(MessageHandler(Filters.text, text))
    # dp.add_error_handler(error)
=======
>>>>>>> 3e0fb57f80371cd707c1c81ab8c4c5acb7035ac3
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
<<<<<<< HEAD
    main()
=======
    main()
>>>>>>> 3e0fb57f80371cd707c1c81ab8c4c5acb7035ac3
