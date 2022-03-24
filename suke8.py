import tweepy

Apikey = "MrXSB2VYQJJYKuLsfbnnG6c2a"
ApikeySecret = "I5Vbo6jpJDNakeyvcggVqSEfWGxmNxyyBabRyu5c1iTrP5TdFs"
AccessToken = "1476512981748187137-KrBrg1JD3adzn58V1ClG9ReFShuIqh"
AccessTokenSecret = "sia6Va8s6AcoDs1ZevZMIg3fI9zMTdMtpo3fVCzM4EOzF"


auth =  tweepy.OAuthHandler(Apikey,ApikeySecret)
auth.set_access_token(AccessToken,AccessTokenSecret)

api = tweepy.API(auth)

objects = api.search_tweets(q="出稼ぎ", count=100)
#print(objects)

for object in objects:

    try:
        retweetId = object.id
        api.retweet(retweetId)

    except tweepy.TweepError as e:
        print(e)
