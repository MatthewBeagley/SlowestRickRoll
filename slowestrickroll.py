import time
from twython import Twython

from os import environ 
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']
# (
#     consumer_key,
#     consumer_secret,
#     access_token,
#     access_token_secret
# )

from lyrics import lyrics

twitter = Twython(
    CONSUMER_KEY,
    CONSUMER_SECRET,
    ACCESS_KEY,
    ACCESS_SECRET
)

while True:
	time.sleep(60)
	temp = lyrics.pop(0)
	twitter.update_status(status=temp)
	print("Tweeted: %s" % temp)
	print(temp)
	lyrics.append(temp)


# message = "Hello world!"
# twitter.update_status(status=message)
# print("Tweeted: %s" % message)