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
    auth = tweepy.OAuthHandler('xIO5AGh0Y1vqczgQmUd2HcDzs', 'aC0HVV8jZ9pHHP5ttW4MkXTP4jIwggPjCnpUKy8ToA4fw8sQYu')
    auth.set_access_token('1297448302682791936-YFZxif5aFoZ0Bg65GKkem4dhUk0We4', 'l3mL77m4cPneZajS0mthMvuKehnpJOW47uxucAgKn5hCZ')

    api = tweepy.API(auth, wait_on_rate_limit=True)

    f = io.open('frases.txt', encoding="utf8").read().splitlines()
    myline =random.choice(f)
    print(myline)

    tweet = ( myline + real) 

    #tweet no ar
    api.update_status(tweet)
    print("Tweet Printado com Sucesso")
    time.sleep(86400)



