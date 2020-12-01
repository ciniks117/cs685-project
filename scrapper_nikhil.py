import os
import tweepy as tw
import pandas as pd
import csv
import datetime
import json

consumer_key      = "kLuVm015U34zoGDgKTVdt09Tr" 
consumer_secret   = "vYS91MtHawRVuP9bL6ApoHkD2A1POfOcMNcpbJ3phn2qh2U8ty"
access_token       = "139643926-WR4ch6ZmLBmf37ImqIkzz0p6XwT51QrE8XQe4DdB"
access_token_secret = "pc4GUZv6k4xTjCRtxxjq6QQf78l9lBn4ZBIFMAvL26QVt"


auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

# Define the search term and the date_since date as variables
#search_words = "#FarmersProtest" #in seq the tweet file is generated
#search_words = "#FarmBills"
#search_words = "#FarmerFirst"
#search_words = "#farmer"
#search_words = "#FarmersWithModi"
#search_words = "#FarmersBill2020"

#search_words = "#HathrasCase"
#search_words = "#HathrasTruthExposed"
#search_words = "#HathrasTapes"

search_words = "#FranceBeheading"
#search_words = "#ViennaTerrorAttack"
search_words = "#ViennaAttack"
#search_words = "#USElection2020"
#search_words = "#USElectionResults2020"
date_since = "2020-11-03"
date_until = "2020-11-04"
suff=datetime.datetime.now().time()
filename = "Tweet_"+search_words+"_"+date_since+"_Nikhil.csv"
# Open/create a file to append data to
csvFile = open(filename, 'a+')
csvWriter = csv.writer(csvFile,delimiter='~')

for tweet in tw.Cursor(api.search,
              q=search_words,
              lang="en",
              until=date_until,
              since=date_since).items():
    newt=tweet._json
    
    data=newt['created_at'],newt['id_str'],newt['text'],newt['geo'],newt['coordinates'],newt['place'],newt['retweet_count'],newt['retweeted'],newt['lang'],newt['user']['location'],newt['user']['id_str'],newt['user']['name'],newt['user']['screen_name'],newt['user']['description'],newt['user']['created_at'],newt['user']['utc_offset'],newt['user']['time_zone'],newt['user']['geo_enabled'],newt['user']['verified'],newt['user']['lang']
    csvWriter.writerow([data])
    #break
    ''' 
    print(newt['id'])
    print(newt['created_at'])
    print(newt['id_str'])
    print(newt['text']) 
    print(newt['user'])
    print(newt['geo'])
    print(newt['coordinates'])
    print(newt['place'])
    print(newt['retweet_count'])
    print(newt['retweeted'])
    print(newt['possibly_sensitive'])
    print(newt['lang'])
    print(newt['user']['location'])
    print(newt['lang'])
    print(newt['user']['id'])
    print(newt['user']['id_str'])
    print(newt['user']['name'])
    print(newt['user']['screen_name'])
    print(newt['user']['location'])
    print(newt['user']['description'])
    print(newt['user']['created_at'])
    print(newt['user']['utc_offset'])
    print(newt['user']['time_zone'])
    print(newt['user']['geo_enabled'])
    print(newt['user']['verified'])
    print(newt['user']['lang'])
    '''
    #csvWriter.writerow([newt['id'],newt['user']['location']])
    print(tweet.created_at)
csvFile.close()


# Collect tweets
# Iterate and print tweets
#for tweet in tweets:
#    #print(tweet)
#    print(tweet.text)
    
# Collect a list of tweets
#t = [tweet.text for tweet in tweets]

#new_search = search_words + " -filter:retweets"
#tweets = tw.Cursor(api.search,
#                       q=new_search,
#                       lang="en",
#                       since=date_since).items(5)
#[tweet.text for tweet in tweets]
'''
search_words = "#NEET"
new_search = search_words + " -filter:retweets"
date_since = "2020-07-15"
tweets = tw.Cursor(api.search, 
                           q=new_search,
                           lang="en",
                           since=date_since).items(50)

#users_locs = [[tweet.user.screen_name, tweet.user.location] for tweet in tweets]
users_locs = [[tweet.user.location] for tweet in tweets]
print(users_locs)
'''
