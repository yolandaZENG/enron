#!/usr/bin/python

from nltk.stem.snowball import SnowballStemmer
import string
import re

def parseOutText(f):
    """ given an opened email file f, parse out all text below the
        metadata block at the top
        (in Part 2, you will also add stemming capabilities)
        and return a string that contains all the words
        in the email (space-separated) 
        
        example use case:
        f = open("email_file_name.txt", "r")
        text = parseOutText(f)
        
        """


    f.seek(0)  ### go back to beginning of file (annoying)
    all_text = f.read()

    ### split off metadata
    content = all_text.split("X-FileName:")
    stemmer=SnowballStemmer("english")
    words = ""
    words_array=[]
    if len(content) > 1:
        ### remove punctuation
        text_string = content[1].translate(string.maketrans("", ""), string.punctuation)

        ### project part 2: comment out the line below
        words_array =re.split(' |\n|\r|\t',text_string)
        #print words_array
        for i in words_array:
            if not i=="":
                words=words+stemmer.stem(i)+" "
        ### split the text string into individual words, stem each word,
        ### and append the stemmed word to words (make sure there's a single
        ### space between each stemmed word)
        
    return words

    

def main():
    ff = open("./test_email.txt", "r")
    print ff.read()
    text = parseOutText(ff)
    print text



if __name__ == '__main__':
    main()
