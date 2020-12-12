import tweepy
import json
from os import environ

def main():
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


    followers = []
    print("after followers dic")
    for page in tweepy.Cursor(api.friends, screen_name='@ZawadHossain12', wait_on_rate_limit=True).pages():
        try:
            followers.extend(page)
        except tweepy.TweepError as e:
            print("Going to sleep:", e)
        print("after loop1")
        for user in followers:
            try:
                print("---------------------------------")
                print("user name:",user.name)
                tweets = api.user_timeline(id=user.id)
                #number of tweet i want to like
                limit = 4
                count = 0
                for tweet in tweets:
                    # api.create_favorite(tweet.id)
                    if tweet.in_reply_to_status_id is not None:
                        continue 
                    if not tweet.favorited:
                        try:
                            tweet.favorite()
                            print('----Liking Tweet-----', tweet.text)
                            print(tweet.favorited)
                            count +=1
                        except Exception as e:
                            print("erron in liking tweet, error: ",e)
                    if count >=limit:
                        break
            except Exception as e:
                print("error in getting tweet, error: ",e)

while(True):
    main()
