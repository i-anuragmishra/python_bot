import json
import urllib
import sys
import time
import tweepy

# enter the corresponding information from your Twitter application/Forecast.io API KEY/lat and long:
CONSUMER_KEY = 'YOUR_CONSUMER_KEY'
CONSUMER_SECRET = 'YOUR_CONSUMER_SECRET'
ACCESS_KEY = 'YOUR_ACCESS_KEY'
ACCESS_SECRET = 'YOUR_ACCESS_SECRET'
FORECAST_IO_APIKEY = 'YOUR_FORECAST_IO_APIKEY'
LATITUDE = 'YOUR_LATITUDE_VALUE'
LONGITUDE = 'YOUR_LONGITUDE_VALUE'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

url = "https://api.forecast.io/forecast/" + \
    FORECAST_IO_APIKEY + "/" + LATITUDE + "," + LONGITUDE
response = urllib.urlopen(url)
data = json.loads(response.read())

# print json.dumps(data, sort_keys=True, indent=4)

temperature = str(int(round(data['currently']['temperature'])))
degree_sign = u'\N{DEGREE SIGN}'
summary = data['daily']['summary']
today = data['hourly']['summary']

tweet = "It's " + temperature + degree_sign + "F. " + today + " " + summary

if len(tweet) > 140:
    tweet = "It's " + temperature + degree_sign + "F. " + today

print tweet
api.update_status(status=tweet)
