
import wget
import tweepy
from tweepy import OAuthHandler
import json
import cv2
import os
from PIL import Image
import pytesseract
import json
import subprocess


def sendmessage(message):
    subprocess.Popen(['notify-send', message])
    return

@classmethod
def parse(cls, api, raw):
    status = cls.first_parse(api, raw)
    setattr(status, 'json', json.dumps(raw))
    return status
 
tweepy.models.Status.first_parse = tweepy.models.Status.parse
tweepy.models.Status.parse = parse
tweepy.models.User.first_parse = tweepy.models.User.parse
tweepy.models.User.parse = parse
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

tweets = api.user_timeline(screen_name='officialmcafee',
                           count=500, include_rts=False,
                           exclude_replies=True)


media_files = set()
for status in tweets:
    media = status.entities.get('media', [])
    if(len(media) > 0):
        media_files.add(media[0]['media_url'])



for media_file in media_files:
    wget.download(media_file)


image = cv2.imread("1.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
filev2 = "mcaffee.png"
print "\n"

cv2.imwrite(filev2, gray)
a=Image.open(filev2)
text = pytesseract.image_to_string(a)
text = text.replace('(',' ')
words = text.split(" ")


with open('cryptocurrencies.json') as json_data:
    d = json.load(json_data)
coin = " "
for word in words:
    if(word in d) :
      coin = word


sendmessage("Coin of the day : " + coin)
sendmessage("Coin of the day : " + coin)
sendmessage("Coin of the day : " + coin)
sendmessage("Coin of the day : " + coin)
sendmessage("Coin of the day : " + coin)
sendmessage("Coin of the day : " + coin)
