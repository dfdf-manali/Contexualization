# from nltk.corpus import wordnet as wn
# from nltk.corpus import sentiwordnet as swn
# print wn.synsets('motorcar')
# print(swn.senti_synset('breakdown.n.03'))
# print(list(swn.senti_synsets('sad')))
# happy = swn.senti_synsets('sad', 'a')
# happy0 = list(happy)[0]
# print(happy0.pos_score())
# print(happy0.neg_score())
# print(happy0.obj_score())
import  preprocessor
import csv
import nltk
import re
data = []
file_path = 'E://twitter10k.csv'
def read_csv(file_path, has_header = True):
    with open(file_path) as f:
        if has_header: f.readline()        
        for line in f:
            line = line.strip().split(",")
            data.append([float(x) for x in line])
            print(line)
    return data

# #Read the tweets one by one and process it



# fp = open('D:\data_attwitter10k.csv', 'r')
# line = fp.readline()
# print(line)
# while line:
#     print(line)
#     processedTweet = processTweet(line)
#     preProcessor = preprocessor.Preprocessor()
#     newTweet = preProcessor.preprocess_text(line,True,True,True,True,0)
#     print(processedTweet)
#     print(newTweet)
#     line = fp.readline()
def preProcessTweets():
    processedTweets=[]
    with open("E:/twitter10k.csv",newline='',encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile,delimiter=',',quotechar='|')

        for row in reader:
            try:
                #print(counter)
                #print(row)
                tweet = row[-2]
                #print(tweet)
                #print('############')
                preProcessor = preprocessor.Preprocessor()
                processedTweet=preProcessor.preprocess_text(tweet)
                #print(processedTweet)
                for word in processedTweet:
                    if(word!='http' and word!='get' and word!='is' and word!='ny' and word!='lol' and word!='lol' and word!='na' and word!='u' and word!='-' and word!='us' and word!='im'):
                        processedTweets.append(word)
                #print('done processing ############')
            except Exception as e:
                i=1
                #print(str(e))

        return processedTweets

processedTweets = preProcessTweets()
freqdist = nltk.FreqDist(processedTweets)
topWords = freqdist.most_common(100)
topWords.insert(0,['keyword','count'])
wfile_path = 'E:/TopKeywords.csv'
with open(wfile_path, 'w', newline='') as fp:
    a = csv.writer(fp, delimiter=',')    
    a.writerows(topWords)
#for t in topWords:
#    print(nltk.pos_tag(t[0]))
#    nltk.pos_tag(t)
#preProcessor = preprocessor.Preprocessor()
def searchTweets(keyword):
    resultTweets=[]
    with open("E:/twitter10k.csv",newline='',encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile,delimiter=',',quotechar='|')

        for row in reader:
            try:                
                tweet = row[-2]
                #print(tweet)
                if tweet.find(keyword) >= 0:                    
                    resultTweets.append(keyword+":"+tweet)
                    
            except Exception as e:
                i=1
                #print(str(e))

        return resultTweets

'''
Search top keywords in tweets and write to .csv
'''
allTweets = []
for i,t in enumerate(topWords):
    result = searchTweets(t[0])
    allTweets.append(result)
tweetfile_path = 'E:/TopKeyTweets.csv'
with open(tweetfile_path, 'w', newline='') as fp:
    a = csv.writer(fp, delimiter='\n')    
    a.writerows(allTweets)

    




