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

for person in [1,118]:   #lay-k 63 skilling 118
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
                text=text.replace(i,"")
            word_data.append(text)
            if person==63 or person== 118:
                word_target.append(1) ###id author
            else:
                word_target.append(0)
                

##########sklearn
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
tfidf=TfidfVectorizer(stop_words="english")
tfidf.fit(word_data)
#print tfidf.transform(word_data)
tf_word_data=tfidf.transform(word_data)
print tf_word_data
####classification ML

clf=MultinomialNB().fit(tf_word_data,word_target)
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


    
def modelPredict(predict_text):
    from os import listdir
    from os.path import isfile,join
    import pickle
    import re
    import sys
    from parse_out import parseOutText
    from nltk.corpus import stopwords
    from sklearn.feature_extraction.text import TfidfVectorizer
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


    file_list=[]
    direc_one=[]
    mypath=direc[0]
    word_data=[]
    word_target=[]
    sw=stopwords.words("english")
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
        email=open( i, "r")
        text=parseOutText(email)

        for s in sw:
            text=text.replace(i,"")
        word_data.append(text)
        word_target.append(0) ###id author

    ##########sklearn

    tfidf=TfidfVectorizer(stop_words="english")
    tfidf.fit(word_data)
    #print tfidf.transform(word_data)
    print tfidf.transform(word_data)

    ####classification ML
    from sklearn.naive_bayes import MultiomialNB
    clf=MultinomialNB().fit(word_data,word_target)
    return clf.predict(predict_text)
#print(file_list)
#print(direc_one)
