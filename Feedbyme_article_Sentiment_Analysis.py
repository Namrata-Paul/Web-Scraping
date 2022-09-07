#!/usr/bin/env python
# coding: utf-8

# In[38]:


from bs4 import BeautifulSoup
import pandas as pd
import requests
import pprint
import re
import textblob


# In[39]:


url='https://www.feedbyme.com/ishwar-chandra-vidyasagar-200th-birth-anniversary/'
req = requests.get(url)
content=req.text


# In[40]:


Soup = BeautifulSoup(content, 'lxml')


# In[41]:


Soup =Soup.getText(strip = True)


# In[42]:


import string
from collections import Counter

import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize


# In[43]:


lower_case = Soup.lower()
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))


# #### Removing stop words from the tokenized words list

# In[44]:


tokenized_words = word_tokenize(cleaned_text, "english")


# #### Removing Stop Words

# In[45]:


final_words = []
for word in tokenized_words:
    if word not in stopwords.words('english'):
        final_words.append(word)


# #### Lemmatization - From plural to single + Base form of a word (example better-> good)

# In[46]:


#import nltk
#nltk.download()


# In[47]:


lemma_words = []
for word in final_words:
    word = WordNetLemmatizer().lemmatize(word)
    lemma_words.append(word)


# In[48]:


emotion_list = []
for line in lemma_words:
        clear_line = line.replace(',', '').replace("'", '').strip()
        
w = Counter(lemma_words)


# In[49]:


def sentiment_analyse(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    print(score)
    if score['neg'] > score['pos']:
        print("Negative Sentiment")
    elif score['neg'] < score['pos']:
        print("Positive Sentiment")
    else:
        print("Neutral Sentiment")


sentiment_analyse(cleaned_text)


# In[ ]:




