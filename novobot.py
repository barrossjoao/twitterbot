#pegando a info do dolar
import tweepy
import requests
from bs4 import BeautifulSoup

page = requests.get("https://dolarhoje.com/")
soup = BeautifulSoup(page.text, 'html.parser')

real = soup.find('input', {'id': 'nacional'})['value']


#bot twitter 
auth = tweepy.OAuthHandler('t17ApwVYGIqBiWWwyxm7p618y', 'cL25YeAAs2fU05OZUzmgZQJkKyEtW08Bq7OBQYPbqwrHsPNHY2')
auth.set_access_token('1297448302682791936-h68CEZeh01vO0t84yPW61s6EnpzvCv', '7eywRpn1cvnm5Izt34a9VUIRyJC7w1JJUNqpJJJMUWizB')

api = tweepy.API(auth, wait_on_rate_limit=True)

tweet = ("A Cotação do Dólar para 1 Real no dia de hoje é " + real) 

api.update_status(tweet)
print("tweet printado com sucesso")
