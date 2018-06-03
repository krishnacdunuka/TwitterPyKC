import tweepy as tw

#keys are stored in a local file keys.py
from keys import *

# Authorizing the Application to your account
auth = tw.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api = tw.API(auth)

# Your Home Timeline:
def home():
    print('Home Timeline:')
    for tweet in tw.Cursor(api.home_timeline).items(10):
        print(tweet.text)

def search(q):
    for tweet in tw.Cursor(api.search, q=q).items(5):
        print(tweet.text)

# Retweet
def retweet(id):
    api.retweet(id=id)
    print('Tweet retweeted!')

# Tweet
def update(status):
    api.update_status(status)
    print('Your tweet has been posted!')

# Delete your last tweet
def delete():
    tweet = api.user_timeline()[0]
    api.destroy_status(tweet.id)
    print('Your last tweet: "' + tweet.text + '" has been deleted')

# Mentions
def mentions():
    print('Your mentions:')
    for mention in tw.Cursor(api.mentions_timeline).items():
        print(mention.text)

# People you follow:
def following():
    print('You follow:')
    # If you have a long following list, add num of followers you want to access as param to items()
    for friend in tw.Cursor(api.friends).items():
        print(friend.name)

# Your followers:
def followers():
    print('People following you:')
    for follower in tw.Cursor(api.followers).items():
        print(follower.name)

#Put function calls here to get your results