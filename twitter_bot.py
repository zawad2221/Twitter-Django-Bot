import tweepy
import json
from os import environ
import time 

class FavRetweetListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
       
        if tweet.in_reply_to_status_id is not None or \
            tweet.user.id == self.me.id:
            # This tweet is a reply or I'm its author so, ignore it
            return
        if tweet.favorited == False:
            # Mark it as Liked, since we have not done it yet
            try:
                tweet.favorite()
                print("liked tweet: ")
            except Exception as e:
                print("Error on fav",e)
                #time.sleep(9)


        if not tweet.retweeted:
             # Retweet, since we have not retweeted it yet
             try:
                 tweet.retweet()
                 your_status = "Hi! I'm a Twitter Bot developed by @ZawadHossain12  to like & retweet #django #python #100DaysOfCode. Follow me to get update about #django #python #100DaysOfCode. If u like it, Give it a star👉( https://github.com/zawad2221/Twitter-Django-Bot )"
                 reply_status = "@%s %s" % (tweet.user.screen_name, your_status)
                 status=reply_status
                 in_reply_to_status_id=str(tweet.id)
                 self.api.update_status(status, in_reply_to_status_id,auto_populate_reply_metadata=True)
                 #self.api.update_status(reply_status,tweet.id)
                 print("retweeted: ") 
             except Exception as e:
                 print("Error on retweet",e)

    def on_error(self, status):
        print(status)

hashtag = ["#Django", "#django", "#DjantweetgoDev", "#djangodev",
 "#python", "#djangounchained", "#pythonprogramming",
  "#DjangoDevelopment", "#PythonProgramming",
 "#djangodevelopment","#DjangoDevelopment","#DjangoDev",
 "#100DaysOfCode","100daysofcode","100daysofcodechallenge"]

def main(keywords):
    CONSUMER_KEY = environ['CONSUMER_KEY']
    CONSUMER_SECRET = environ['CONSUMER_SECRET']

    ACCESS_KEY = environ['ACCESS_KEY']
    ACCESS_SECRET = environ['ACCESS_SECRET']
    

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    try:
        api.verify_credentials()
        print("authentication ok")
    except:
        print("error during authentication")
        return

    tweets_listener = FavRetweetListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=keywords, languages=["en"])
 
          


main(hashtag)
