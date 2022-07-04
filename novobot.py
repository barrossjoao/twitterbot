import tweepy
import requests
from bs4 import BeautifulSoup
import time
import random
import io

#pegando a info do dolar
while True:


    page = requests.get("https://dolarhoje.com/")
    soup = BeautifulSoup(page.text, 'html.parser')

    real = soup.find('input', {'id': 'nacional'})['value']


    #bot twitter 
    auth = tweepy.OAuthHandler("EC3YctFG7y9lQT7aQaApqVeAT", "0awS4t9pPe9GhHRBIIcIrJ8ptk43qxaaMReGhMOo6oJOhptT5s")
    auth.set_access_token("1297448302682791936-zxIeFBZW74Lpmizu8EoL5ZSsrwj5rO", "5MtKma7yA1ppC6wiAnktA0rJieHlKP5IqHlVyGhopCivV")

    api = tweepy.API(auth, wait_on_rate_limit=True)

    #file 
    f = io.open('frases.txt', encoding="utf8").read().splitlines()
    myline =random.choice(f)

    tweet = ( myline + real) 

    #tweet no ar
    api.update_status(tweet)
    print("Tweet Printado com Sucesso")
    time.sleep(86400)



