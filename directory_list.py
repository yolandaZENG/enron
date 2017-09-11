#!/usr/bin/python
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
