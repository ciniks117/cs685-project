from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
import csv
import re
#Dfilename="Test_Data.csv";
Dfilename="Farmer-Tweets.csv";
Dfile=open(Dfilename,"r",encoding="utf-8");
Data=[];
csvReader=csv.reader(Dfile);

def preprocess_word(word):
    # Remove punctuation
    word = word.strip('\'"?!,.():;')
    # Convert more than 2 letter repetitions to 2 letter
    # funnnnny --> funny
    word = re.sub(r'(.)\1+', r'\1\1', word)
    # Remove - & '
    word = re.sub(r'(-|\')', '', word)
    return word

def is_valid_word(word):
    # Check if word begins with an alphabet
    return (re.search(r'^[a-zA-Z][a-z0-9A-Z\._]*$', word) is not None)

def handle_emojis(tweet):
    # Smile -- :), : ), :-), (:, ( :, (-:, :')
    tweet = re.sub(r'(:\s?\)|:-\)|\(\s?:|\(-:|:\'\))', ' EMO_POS ', tweet)
    # Laugh -- :D, : D, :-D, xD, x-D, XD, X-D
    tweet = re.sub(r'(:\s?D|:-D|x-?D|X-?D)', ' EMO_POS ', tweet)
    # Love -- <3, :*
    tweet = re.sub(r'(<3|:\*)', ' EMO_POS ', tweet)
    # Wink -- ;-), ;), ;-D, ;D, (;,  (-;
    tweet = re.sub(r'(;-?\)|;-?D|\(-?;)', ' EMO_POS ', tweet)
    # Sad -- :-(, : (, :(, ):, )-:
    tweet = re.sub(r'(:\s?\(|:-\(|\)\s?:|\)-:)', ' EMO_NEG ', tweet)
    # Cry -- :,(, :'(, :"(
    tweet = re.sub(r'(:,\(|:\'\(|:"\()', ' EMO_NEG ', tweet)
    return tweet


def preprocess_tweet(tweet):
    processed_tweet = []
    # Convert to lower case
    tweet = tweet.lower()
    # Replaces URLs with the word URL
    tweet = re.sub(r'((www\.[\S]+)|(https?://[\S]+))', ' URL ', tweet)
    # Replace @handle with the word USER_MENTION
    tweet = re.sub(r'@[\S]+', 'USER_MENTION', tweet)
    # Replaces #hashtag with hashtag
    tweet = re.sub(r'#(\S+)', r' \1 ', tweet)
    # Remove RT (retweet)
    tweet = re.sub(r'\brt\b', '', tweet)
    # Replace 2+ dots with space
    tweet = re.sub(r'\.{2,}', ' ', tweet)
    # Strip space, " and ' from tweet
    tweet = tweet.strip(' "\'')
    # Replace emojis with either EMO_POS or EMO_NEG
    tweet = handle_emojis(tweet)
    # Replace multiple spaces with a single space
    tweet = re.sub(r'\s+', ' ', tweet)
    words = tweet.split()

    for word in words:
        word = preprocess_word(word)
        if is_valid_word(word):
            processed_tweet.append(word)
    return ' '.join(processed_tweet)

def Preprocess_All_Tweets(Data):
    NewData=[];
    for tweet in Data:
        tweet=list(tweet);
        tweet_text=tweet[2];
        cleaned_tweet_text=preprocess_tweet(tweet_text);
        tweet[2]=cleaned_tweet_text;
        tweet=tuple(tweet);
        NewData.append(tweet)
    return NewData;

def Sentiment_Analyser(Data):
    NewData=[];
    sentiment_analyzer=NaiveBayesAnalyzer();
    for tweet in Data:
        tweet=list(tweet);
        tweet_text=tweet[2];
        blob = TextBlob(tweet_text, analyzer=sentiment_analyzer);
        #blob.sentiment is tuple of size 3. first element contain pos or neg, 2nd pobabilty of Positive and 3rd probabilty of neg 
        tweet.append(blob.sentiment[0])
        print(blob.sentiment)
        tweet=tuple(tweet);
        NewData.append(tweet)
    return NewData;


if __name__ == '__main__':
    #Reading tweets into variable Data
    print("Reading Data from File")
    for row in csvReader:
        Data.append(eval(row[0]));
    print("Reading Done");
    print("Preprocessing Tweets")
    NewData=Preprocess_All_Tweets(Data);
    print("Preprocessing Done")
    #Applying Sentiment Analysis on Tweets
    print("Calclating Sentiments")
    Sentiment_Data=Sentiment_Analyser(NewData);
    print("Sentiment Aalysis Done")
