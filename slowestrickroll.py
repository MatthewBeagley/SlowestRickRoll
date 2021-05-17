import time
import datetime
import credentials
import tweepy
import numpy as num


#set api credentials
CONSUMER_KEY = credentials.consumer_key
CONSUMER_SECRET = credentials.consumer_secret
ACCESS_KEY = credentials.access_token
ACCESS_SECRET = credentials.access_token_secret

#intialize api
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)

#open file
fileObj = open("lyrics.txt", "r")
words = fileObj.read().splitlines()
fileObj.close()

#tweet
temp = words.pop(0)
api.update_status(temp)
words.append(temp)

#debug messages
print("Tweeted: %s" % temp)
print(datetime.datetime.now())

#save to file
num.savetxt("lyrics.txt", words, delimiter=" ", fmt="%s")
