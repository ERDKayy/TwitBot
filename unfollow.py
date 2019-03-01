import tweepy
import schedule
import time
import sys
import datetime
import random
import json

with open('key_file.json', 'r') as fp:
    keys = json.load(fp)

consumer_key = keys["consumer_key"]
consumer_secret = keys["consumer_secret"]
access_token = keys["access_token"]
access_token_secret = keys["access_token_secret"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

print(">>>>> | Unfollow.py | Begin")

user = api.me()
friends = api.friends_ids('E R D K')

keepFollowing = ['4140881832', '935819617909530625', '827176049553256450', '827883145504645124', '2996620543', '25680860', '550605277', 
'2708191476', '44293006', '15746580', '720303639277928448', '24613879', '14874142', '22637974', '2559865245', '1452520626', '15901272', 
'15567576', '1043233982303887361', '3028352708', '2344952971', '4095043094', '13610342', '3375660701', '1955411096', '63796828', '202463874', 
'4398545955', '246596682', '17915692', '31233851', '2361438475', '2997658879', '15680204', '244441120', '371230439', '161418822', '1118893002', 
'1902865520', '2472089628', '2917301712', '4767225325', '2918927984', '818576939233386497', '72415936', '257283408', '3227981912', '312937997', 
'357294577', '1729518109', '598642412', '607327599', '842072275', '2222629992', '80420672', '3906765817', '1124722303', '386772363', '66629039', 
'3486875477', '1094966674321797121', '978162872294391810', '2458339836', '1726152630', '842474623', '1071104846684676104', '1747473110', '1488707239', 
'268479669', '3225436049', '1048018930785083392', '701658616839872517', '1083133076547395585', '986057666668609536', '1046573157061136384', 
'910654040794570752', '3240883212', '37582029', '287455903', '3359438776', '958923426906882048', '2244953047', '214201922', '1492124791', 
'937401196196720640', '919456188483256320', '3002817576', '2823705300', '944171449', '887808792041148416', '1027859204', '894984751240560640', 
'826127947635453952', '1542453360', '309366491']


for x in range(100):
    toUnfollow = random.choice(friends)
    userID = str(toUnfollow)
    if userID not in keepFollowing:
        print(">>>>> | Unfollow.py | Unfollowing {0}".format(api.get_user(toUnfollow).screen_name))
        try: 
            api.destroy_friendship(toUnfollow)
            time.sleep(random.randint(1,8))
            
        except tweepy.TweepError as e:
            print(e.reason)

        except StopIteration:
            break
    else: 
        print(">>>>> | Unfollow.py | Skipped: {0} -".format(api.get_user(toUnfollow).screen_name) + "They're on your 'do not unfollow' list")
        time.sleep(random.randint(1,3))

print(">>>>> | Unfollow.py | End")