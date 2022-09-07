#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import pandas as pd
import requests
import pprint
import re
import textblob


# In[2]:


url='https://www.feedbyme.com/ishwar-chandra-vidyasagar-200th-birth-anniversary/'
req = requests.get(url)
content=req.text


# In[3]:


soup = BeautifulSoup(content, 'lxml')


# In[4]:


soup =soup.getText(strip = True)


# In[5]:


soup


# In[6]:


soup = re.sub(r'\[\d+\]', "", soup)


# In[7]:


soup = re.sub(r'\[\w+\]', "", soup)


# In[8]:


soup = re.sub('[0-9]+', "", soup)


# In[9]:


soup


# In[10]:


import nltk


# In[11]:


#nltk.download()


# In[12]:


from nltk.tokenize import sent_tokenize


# In[13]:


#nltk.download('punkt')


# In[14]:


sentence = sent_tokenize(soup)
len(sentence)


# In[15]:


sentence


# In[16]:


from nltk.tokenize import word_tokenize


# In[17]:


s_words = word_tokenize(soup)
s_words = [word for word in s_words if word.isalnum()]


# In[18]:


from nltk.corpus import stopwords


# In[19]:


stop_words = set(stopwords.words('english'))
s_words = [word for word in s_words if not str.lower(word) in stop_words]


# In[20]:


from textblob import TextBlob


# In[21]:


def sentiment_analysis(article):
    analysis = TextBlob(article)
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    elif analysis.sentiment.polarity == 0:
        return 'Neutral'
    else:
        return 'Negative'


# In[22]:


sentence = pd.DataFrame(sentence)
sentence.columns = ['sentence']
sentence['sentiment'] = [str(sentiment_analysis(x)) for x in sentence.sentence]
sentence.sentiment.value_counts()


# In[23]:


#nltk.download('stopwords')


# In[24]:


from nltk.probability import FreqDist


# In[25]:


wordfreq = FreqDist(s_words)


# In[26]:


wordfreq


# In[ ]:




