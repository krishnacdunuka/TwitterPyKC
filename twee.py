import tweepy as tw
import webbrowser as wb

# Storing key inputs from user
consumer_key = input('Cosumer key: ').strip()
consumer_secret = input('Consumer secret key: ').strip()

# Authorizing the Application to your account
auth = tw.OAuthHandler(consumer_key, consumer_secret)

wb.open(auth.get_authorization_url())
pin = input('Authorization PIN: ')
access_token, access_token_secret = auth.get_access_token(verifier = pin)

auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth)

# Your Home Timeline:
def home():
    print('Home Timeline:')
    for tweet in tw.Cursor(api.home_timeline).items(10):
        print('TweetID:', tweet.id, tweet.text)

# Retweet
def retweet(id):
    api.retweet(id=id)
    print('Tweet retweeted!')

# Unretweet
def unretweet(id):


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

if __name__ == '__main__':
    while(True):
        action = input('Enter your query: ')
        if action == 'update': update(input('What\'s happening?\n'))
        elif action == 'home': home()
        elif action == 'retweet': retweet(input('Tweet ID: '))
        elif action == 'delete': delete()
        elif action == 'following': following()
        elif action == 'followers': followers()
        else: break
