from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pandas as pd
import csv

#instantiate classifier and vectorizer
clf=MultinomialNB(alpha=.01)
vectorizer =TfidfVectorizer(min_df=1,ngram_range=(1,2))

#Apply vectorizer to training data
df = pd.read_excel("E:/Offers.xlsx", sep=",")
offers = list(df["OfferDescription"])
#print(offers)
#traindata=['Extra 25% off your next purchase on already discounted merchandise at music cds','Buy music cd and get t-shrit free','i do not know','i am not sure','i have no idea','i'];
traindata = offers

X_train=vectorizer.fit_transform(traindata)
#print(X_train)

#Offer Ids
y_train=list(range(len(offers)))

#Train classifier
clf.fit(X_train, y_train)

tt = pd.read_csv("E:\\TopTweets.csv", sep=",")
#print(tt["Tweets"])
topTweets = []
for t in list(tt["Tweets"]):
    #print(t.split(":")[1])
    topTweets.append(t.split(":")[1])
#print(topTweets) 
#print(clf.predict(vectorizer.transform(['@nathankmusic @yungDobis Im too stoned to talk about Doritos right now.'])))

allOffers = list()
for t in topTweets:
    o = offers[clf.predict(vectorizer.transform([t]))]
    allOffers.append("Tweet:"+t + ",offer:" + o)
    #print(t + ",offer:" + o)

tweetfile_path = 'E:/SortedOffers.csv'
with open(tweetfile_path, 'w', newline='\n') as fp:
    a = csv.writer(fp,delimiter='\n')
    #for o in allOffers:
    a.writerows([allOffers])
print(allOffers[0])
#print(clf.predict(vectorizer.transform(['I am not able to find good music cd'])))
