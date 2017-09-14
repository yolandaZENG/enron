#!/usr/bin/python

def nlp_predict(input_text):
    from os import listdir
    from os.path import isfile,join
    import pickle
    import re
    import sys
    import numpy as np
    from parse_out import parseOutText
    from nltk.corpus import stopwords
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn import metrics
    from sklearn.feature_extraction.text import CountVectorizer
    from sklearn.naive_bayes import MultinomialNB
    from sklearn.externals import joblib
    tf=joblib.load("tf.pkl")
    clf=joblib.load("clf.pkl")
    word_data=[]
    word_predict=[]
    print(input_text)
    sw=stopwords.words("english")
    for s in sw:
        input_text=input_text.replace(s,"")
    word_data.append(input_text)
    tf_word_data=tf.transform(word_data)
    word_predict=clf.predict(tf_word_data)
    return word_predict[0]


email='''This is just the beginning!  We have created a committee that is dedicated to improving the Accounts Payable process.  We hope to engage you in this effort and plan to actively seek your involvement and input.  We look forward to working with and hearing from you about future enhancements that will enable iPayit to play a valuable role in your invoice payment activities.
For invoice payment status please call the AP Call Center at (713) 853-7127 or toll free  (866) AP ENRON, or send an e-mail to <mailto:ipayit@enron.com>. '''
print(nlp_predict(email))

email2="hello"
print(nlp_predict(email2))
