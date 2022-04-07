import tweepy
import requests
from bs4 import BeautifulSoup
import time
import random
import io
import keys

#pegando a info do dolar
while True:


    page = requests.get("https://dolarhoje.com/")
    soup = BeautifulSoup(page.text, 'html.parser')

    real = soup.find('input', {'id': 'nacional'})['value']


    #bot twitter 
    auth = tweepy.OAuthHandler(keys.key, keys.secret)
    auth.set_access_token(keys.token, keys.token_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True)

    #file 
    f = io.open('frases.txt', encoding="utf8").read().splitlines()
    myline =random.choice(f)

    tweet = ( myline + real) 

    #tweet no ar
    api.update_status(tweet)
    print("Tweet Printado com Sucesso")
    time.sleep(86400)



