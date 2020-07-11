import nltk
from nltk.corpus import twitter_samples
import matplotlib.pyplot as plt
import random

# nltk.download('twitter_samples')

all_positive_tweets = twitter_samples.strings('positive_tweets.json')
all_negative_tweets = twitter_samples.strings('negative_tweets.json')

print('Number of positive tweets: ', len(all_positive_tweets))
print('Number of negative tweets: ', len(all_negative_tweets))

print('\nThe type of all_positive_tweets is: ', type(all_positive_tweets))
print('\nThe type of tweets_entry is: ', type(all_negative_tweets[0]))
