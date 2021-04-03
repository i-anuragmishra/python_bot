import tweepy
consumer_key = 'IfJZVRHEUajEvQXa3nMdke7cq'
consumer_secret = 'B2c1wjpJdDS34x5c3wqOgQ3o64KydTWIVWZdiI7Xnhaqr9rU2T'
key = '1131296400749154304-7JIXZhqfYiEE32m35vQuUCg1R4s8uQ'
secret = 'PKgsj8ORsebCivylOnM0pbaKqHHv9NKK38Ar3tBFtsx1g'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)
api.update_status('Hello Twitter i am cloudy the Bot')
