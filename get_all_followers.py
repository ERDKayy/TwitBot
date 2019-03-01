import tweepy
import pandas as pd
import json

with open('key_file.json', 'r') as fp:
    keys = json.load(fp)

consumer_key = keys["consumer_key"]
consumer_secret = keys["consumer_secret"]
access_token = keys["access_token"]
access_token_secret = keys["access_token_secret"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


def lookup_user_list(user_id_list, api):
    full_users = []
    users_count = len(user_id_list)
    try:
        for i in range(int((users_count / 100) + 1)):
            print(i)
            full_users.extend(api.lookup_users(user_ids=user_id_list[i * 100:min((i + 1) * 100, users_count)]))
        return full_users
    except tweepy.TweepError:
        print('Something went wrong, quitting...')




api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
user = api.me()
ids = []
for page in tweepy.Cursor(api.friends_ids, screen_name='E R D K').pages():
    ids.extend(page)

results = lookup_user_list(ids, api)
all_users = [{'id': user.id}
             for user in results]

with open('your_file.txt', 'w') as f:
    for item in all_users:
        f.write("%s\n" % item)
