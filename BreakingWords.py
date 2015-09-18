import nltk
from nltk.corpus import wordnet

def is_word(word):
     if not wordnet.synsets(word):
         #print 'Not an English Word',word_to_test
         return 0
     else:
         #print 'an English Word',word_to_test
         return 1
        
word_to_test='CriticsChoice'
# AmericanSniper CriticsChoice
word_to_test=word_to_test.lower()
#print word_to_test
def check(word_to_test):
     if is_word(word_to_test)!=1:
         for i in range(2,len(word_to_test)):
             word=word_to_test[0:i]
     #print word
             if is_word(word):
         #print word,word_to_test[i:len(word_to_test)],i
                 if is_word(word_to_test[i:len(word_to_test)+1]):
                     print word,word_to_test[i:len(word_to_test)]
     else:
         print word_to_test


#calling the function
check('CriticsChoice')