
import nltk
import string
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from collections import Counter
from collections import OrderedDict
import GensimTopic
from operator import itemgetter
stop_word= stopwords.words('english')
file_data_path = '/home/prateek/as.txt'
file= open(file_data_path, 'r')
#print file
i=0
list=[]
document=[]
newlist=[]
freq_map={}
def findingTopics(line):
     #for line in file:
     sentence=[]
     #print line
     text=line.translate(string.maketrans("!~$/#@%':+?).,-(;*&\\\"","                     "), string.digits)
     #print type(text)
     text=text.lower()
     line=text.split()
     
     for word in line:
         pos_tag=nltk.pos_tag(line) 
         if word not in stop_word and  word.startswith('htt') is False  and len(word)>=3 and word.encode('string_escape').find(r'\x')==-1:
             word_list=word.split()
             pos_tag=nltk.pos_tag(word_list)
             #print pos_tag,word
             tag=pos_tag[0]
             tag=str(tag[1])
             #print type(tag)
             if tag.startswith('NN') is False:
                 #print word,tag
                 newlist.append(word)
     #print newlist
     #newlist = ' '.join(newlist)
     #document.append(newlist)
     for word in range(len(newlist)-1): 
         compound_word =newlist[word]
         if freq_map.has_key(compound_word):
             freq_map.update({compound_word:freq_map.get(compound_word)+1})
         else:
             freq_map.update({compound_word:1})
#print newlist

j=0
tweets=[]
for line in file:
     first_name='bradley'
     last_name='cooper'
     sentence=[]
     #print line
     text=line.translate(string.maketrans("!~$/#@%':+?).,-(;*&\\\"","                     "), string.digits)
     #print type(text)
     text=text.lower()
     line=text.split()
     for word in range(len(line)-1):
         if line[word]==first_name  or   line[word+1]==last_name:
             n_line=[]
             for word in line:
                 #print word
                 if wordnet.synsets(word):
                     n_line.append(word)
             line_for_topic=' '.join(n_line)
             tweets.append(line_for_topic)
             #print line_for_topic
             findingTopics(line_for_topic)

topic=GensimTopic.finding_topics(newlist)
#print topic[0]
trending_topic={}
for tweet in tweets: 
     tweet=tweet.split()
     pos_tag=nltk.pos_tag(tweet)
     for l in range(len(pos_tag)-1):
         if pos_tag[i][0] in topic:
             #if pos_tag[i][1]=='JJ'  :
             compound_word=pos_tag[i][0]+'_'+pos_tag[ i+1][0]
             if trending_topic.has_key(compound_word):
                 trending_topic.update({compound_word:trending_topic.get(compound_word)+1})
             else:
                 trending_topic.update({compound_word:1})
j=0

d_sorted_by_value = OrderedDict(sorted(trending_topic.items(), key=itemgetter(1), reverse=True))
for k, v in d_sorted_by_value.items():
     print "%s: %s" % (k, v)
     j=j+1
     if j>=5:
         break
