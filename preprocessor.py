import nltk
import re
class Preprocessor:

    def __init__(self):
         self.stopwords = nltk.corpus.stopwords.words('english')
         self.stopwords.append('url')
         self.stopwords.append('at_user')
         self.stopwords.append('http')
         self.stemmer = nltk.PorterStemmer()

    def cleanTweet(self,tweet):
        # process the tweets

        #Convert to lower case
        tweet = tweet.lower()
        #Convert www.* or https?://* to URL
        tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL',tweet)
        tweet = re.sub('((www\.[^\s]+)|(http?://[^\s]+))','URL',tweet)
        #Convert @username to AT_USER
        tweet = re.sub('@[^\s]+','AT_USER',tweet)
        #Remove additional white spaces
        tweet = re.sub('[\s]+', ' ', tweet)
        #Replace #word with word
        tweet = re.sub(r'([^\s]+)', r'\1', tweet)
        #trim
        tweet = tweet.strip('\'"')
        return tweet

    def tokenize_tokens(self,text):
        return nltk.tokenize.word_tokenize(text)


    def tokenize_sentences(self,text):
        return nltk.tokenize.sent_tokenize(text)

    def fold_case(self,tokens):
        return [tok.lower() for tok in tokens]


    def remove_stop_words(self,tokens):
        return [t for t in tokens if t.lower() not in self.stopwords]

    def is_stop_word(self,token):
        return token.lower() in self.stopwords


    def stem(self,tokens):
        return [self.stemmer.stem(t) for t in tokens]

    def filter_tokens(self,tokens, min_size=0, special_chars=False):
        if min_size>0:
            tokens = [t for t in tokens if len(t) >= min_size]
        if special_chars:
            tokens = [t for t in tokens if re.search('[^a-zA-Z-]',t)==None]
        return tokens

    def preprocess_token(self,token, do_stop_word_removal=True, do_stemming=True, fold=True, specials=True, min_size=3):
        if fold: token = self.fold_case([token])[0]
        if do_stop_word_removal and self.is_stop_word(token): return None
        if do_stemming: token = self.stem([token])[0]
        filt = self.filter_tokens([token], min_size, specials)
        if len(filt)==0: return None
        else: return filt[0]

    def preprocess_text(self,text, do_stop_word_removal=True, do_stemming=True, fold=True, specials=True, min_size=3):
        #print("preprocessing")
        ts = self.cleanTweet(text)
        ts = self.tokenize_tokens(text)
        ts = self.filter_tokens(ts, min_size=min_size,special_chars=specials)
        if fold:
            ts = self.fold_case(ts)
        if do_stop_word_removal:
            ts = self.remove_stop_words(ts)
        if do_stemming:
            ts = self.stem(ts)
        return ts

















