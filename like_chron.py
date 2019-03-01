import tweepy
import schedule
import time
import sys
import datetime
import json, codecs
import random
import logging


logging.basicConfig(filename='likeAndFollowChron.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

with open('key_file.json', 'r') as fp:
    keys = json.load(fp)

consumer_key = keys["consumer_key"]
consumer_secret = keys["consumer_secret"]
access_token = keys["access_token"]
access_token_secret = keys["access_token_secret"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

user = api.me()
username = user.name





print(">>>>> LikeChron | Begin | On user: " + username + " at " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))

def likeRecentTweets(accountID):
    for t in tweepy.Cursor(api.user_timeline, id=accountID, result_type='recent').items(5):
        try:
            t.favorite()
            print('>>>>> LikeChron | likeRecentTweets Function | Liked tweet on user: ' + t.user.screen_name)
        except tweepy.TweepError as e:
            print('>>>> LikeChron | likeRecentTweets Function | Skipping like :' + e.reason)
        except StopIteration:
            break
        time.sleep(2)

def getKeyword(searchStrings):
    choice = random.choice(searchStrings)
    return choice


def job():
    searchStrings = ['ApexLegends', 'Twitch', 'TwitchStreamer', 'LiveStreamer', 'BattleRoyale']
    searchCount = 20
    tweetid = 1


    keyword = getKeyword(searchStrings)

    for tweet in tweepy.Cursor(api.search, 
                                keyword, 
                                result_type='recent',
                                lang="en").items(searchCount):
            try:
                
                #Favorite
                print(">>>>> LikeChron | Like Recent Keyword Tweet | On user: " + tweet.user.screen_name + " at " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
                tweet.favorite()
                time.sleep(3)

                if tweetid % 3 == 0:
                    # Assign the tweets id to a variable so I can like their 5 newest tweets and follow their account.
                    accountToFollow = tweet.user.id
                    tweet.user.follow()
                    likeRecentTweets(accountToFollow)
                    
                    print('>>>>> LikeChron | Follow User | On user: ' + str(tweet.user.screen_name) +  datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
            
            except tweepy.RateLimitError:
                time.sleep(15*60)

            except tweepy.TweepError as e:
                print(e.reason)

            except StopIteration:
                break
            tweetid += 1

    print('>>>>> LikeChron | End | ' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))

schedule.every(18).minutes.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)