#!/usr/bin/env python
import tweepy, random,time
from datetime import datetime
from keys import keys
from qod import getQuote

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']
# datetime object containing current date and time
datetime = datetime.now()

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
 
# twt = api.search("@provjateng",result_type="new",count=5) 
# twt = api.user_timeline("provjateng",count=1000)
# sts = getQuote()
# api.update_status(status=getQuote())
file = open("log","a") 
try:
    sts = getQuote()
    sts = str(sts)+" #quoteoftheday"
    api.update_status(status=sts)
    file.write(str(datetime)+"|SUKSES|"+sts+"\n")
except tweepy.TweepError as e:
    file.write(str(datetime)+"|ERROR|"+str(e)+"\n")
except tweepy.RateLimitError as limit:
    file.write(str(datetime)+"|LIMIT|"+str(limit)+"\n")
    time.sleep(15 * 60)
finally:
    file.close()
# for s in twt:
#     #    print(s.id)
    
#     # sn = s.user.screen_name
#     # m = "@%s " %sn + random.choice(open('tweets.txt').readlines()).strip("\n") 
#     # #    api.update_status(status=m, in_reply_to_status_id = s.id)
#     try:
#         api.create_favorite(s.id)
#         print("++++++++++++++++++++++++++++++++++++++++")
#         print("Sukses like!")
#         print(s.user.screen_name)
#         print(s.text)
#         print("++++++++++++++++++++++++++++++++++++++++")
#     except tweepy.TweepError :
#         print("++++++++++++++++++++++++++++++++++++++++")
#         print("Sudah di like!")
#         print(s.user.screen_name)
#         print(s.text)
#         print("++++++++++++++++++++++++++++++++++++++++")
    
# print("Done!!!")