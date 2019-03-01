import tweepy
import schedule
import time
import sys
import datetime
import json, codecs
import random
import logging

with open('key_file.json', 'r') as fp:
    keys = json.load(fp)

consumer_key = keys["consumer_key"]
consumer_secret = keys["consumer_secret"]
access_token = keys["access_token"]
access_token_secret = keys["access_token_secret"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)


print(api.rate_limit_status())
# print(data['resources']['statuses']['/statuses/home_timeline'])
# print(data['resources']['users']['/users/lookup'])