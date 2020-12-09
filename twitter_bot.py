import tweepy
import json
from os import environ

class FavRetweetListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
       
        if tweet.in_reply_to_status_id is not None or \
            tweet.user.id == self.me.id:
            # This tweet is a reply or I'm its author so, ignore it
            return
        if not tweet.favorited:
            # Mark it as Liked, since we have not done it yet
            try:
                tweet.favorite()
                print("liked tweet: ",tweet.text)
            except Exception as e:
                print("Error on fav",e)
        # if not tweet.retweeted:
        #     # Retweet, since we have not retweeted it yet
        #     try:
        #         tweet.retweet()
        #     except Exception as e:
        #         logger.error("Error on fav and retweet", exc_info=True)

    def on_error(self, status):
        print(status)

hashtag = ["#Django", "#django", "#DjantweetgoDev", "#djangodev",
 "#python", "#djangounchained", "#pythonprogramming",
  "#DjangoDevelopment", "#PythonProgramming",
 "#djangodevelopment","#DjangoDevelopment","#DjangoDev",
 "#androiddevelopment","#androiddev","#AndroidDev","#AndroidDevelopment",
 "#androidstudio","#java","#Java",
 "#javaprogramming","#JavaProgramming","#JavaDevelopment",
 "#javadevelopment","#kotlin","#Kotlin","#kotlindev","#KotlinDev",
 "#kotlindevelopment","#AndroidDev"]

def main(keywords):
    CONSUMER_KEY = environ['CONSUMER_KEY']
    CONSUMER_SECRET = environ['CONSUMER_SECRET']

    ACCESS_KEY = environ['ACCESS_KEY']
    ACCESS_SECRET = environ['ACCESS_SECRET']

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
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
