#!/usr/bin/python
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


file=[]
direc=[]
mypath="/Users/zengyanqing/Desktop/enron/maildir"

for f in listdir(mypath):
    join_f=join(mypath,f)
    if isfile(join_f):
        if cmp(f,".DS_Store") != 0 :           
            file.append(join(mypath,f))
    else:
        direc.append(join_f)


#print(file)
#print(direc)
word_data=[]
word_target=[]
word_predict=[]
sw=stopwords.words("english")

for person in [1,2,3,4,5,10,63,118]:   #lay-k 63 skilling 118
    file_list=[]
    direc_one=[]
    mypath=direc[person]
    person_name=re.split('/',mypath)[-1]
    print(person_name)
    
    #print(mypath)
    for f in listdir(mypath):
        join_f=join(mypath,f)
        if isfile(join_f)==False:
            direc_current=join_f
            for f_current in listdir(direc_current):
                if cmp(f_current,".DS_Store") != 0 :  
                    join_current=join(direc_current,f_current)                
                    file_list.append(join_current)

    for i in file_list:
        text=""
        if isfile(i)==True:
            email=open( i, "r")
            text=parseOutText(email)

            for s in sw:
                text=text.replace(s,"")
            word_data.append(text)
            if person==63 or person== 118:
                word_target.append(1) ###id author
            else:
                word_target.append(0)
                

##########sklearn
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.externals import joblib

tfidf=TfidfVectorizer(stop_words="english")
tfidf.fit(word_data)

#print tfidf.transform(word_data)
tf_word_data=tfidf.transform(word_data)
joblib.dump(tfidf,'tf.pkl')
print(tf_word_data)
####classification ML

clf=MultinomialNB().fit(tf_word_data,word_target)
joblib.dump(clf,'clf.pkl')

word_predict=clf.predict(tf_word_data)
print(word_predict)
print(metrics.confusion_matrix(word_target,word_predict))


print("EXEMPLE TEST")
word_data=[]
#word_data.append('money laundry skilling joh')
word_data.append('hello')
word_test=tfidf.transform(word_data)
word_predict=clf.predict(word_test)
print(word_predict)


    
