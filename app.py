from chalice import Chalice
from twython import Twython, TwythonError
from chalicelib import *

app = Chalice(app_name='hasbi-Allah')


def tweet_hasbi_Allah(hasbana):
    twitter = Twython(api_key, api_secret_key, api_token, api_secret_token)
    try:
        twitter.update_status(status=hasbana)
    except TwythonError as e:
        print(e)

@app.schedule('cron(0 07 ? * * *)')
def morning_hasbana(event):
    hasbana = 'صباح الخير يا جماعة، حسبي الله ونعم الوكيل'
    tweet_hasbi_Allah(hasbana)

@app.schedule('cron(0 19 ? * * *)')
def evening_hasbana(event):
    hasbana = 'مساء الخير يا جماعة، حسبي الله ونعم الوكيل'
    tweet_hasbi_Allah(hasbana)