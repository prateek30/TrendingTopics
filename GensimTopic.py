
import gensim
from gensim import corpora, models, similarities
from gensim.models import hdpmodel, ldamodel
from itertools import izip
import numpy as np
from nltk.corpus import stopwords

stop = stopwords.words('english')

#documents=['american', 'sniper', 'american', 'sniper', 'doesn', 'make', 'proud', 'american', 'probably', 'need', 'check', 'pulse', 'merica', 'dbkkzbfwa', 'retweet', 'going', 'see', 'movie', 'american', 'sniper', 'qniawjj', 'retweet', 'going', 'see', 'movie', 'american', 'sniper', 'aqataovep', 'retweet', 'going', 'see', 'movie', 'american', 'sniper', 'cydwizxcsw', 'fav', 'going', 'see', 'movie', 'american', 'sniper', 'dxwisqjw', 'watched', 'american', 'sniper', 'see', 'bradley', 'cooper', 'movie', 'performance', 'next', 'level', 'know', 'jesseventura', 'sued', 'fallen', 'seal', 'estate', 'americansniper', 'worthless', 'piece', 'shameless', 'american', 'sniper', 'kind', 'reminds', 'movie', 'showing', 'third', 'act', 'inglorious', 'basterds', 'see', 'american', 'sniper', 'powerful', 'movie', 'bradley', 'cooper', 'hard', 'eyes', 'either', 'american', 'sniper', 'akgzpwli', 'fwgvmvra', 'xethsjetei', 'qowwnevl', 'bradley', 'cooper', 'killed', 'role', 'american', 'sniper', 'mad', 'respect', 'wanna', 'feel', 'old', 'american', 'sniper', 'baby', 'looks', 'like', 'qlqkbxfpj', 'ultimate', 'respect', 'chris', 'kyle', 'rip', 'solider', 'americansniper', 'xuwoykitv', 'american', 'sniper', 'tfzfvzhuc', 'wyklezlwol', 'thought', 'american', 'sniper', 'didn', 'come', 'january', 'sotkwwzzbd', 'getting', 'emotional', 'see', 'american', 'sniper', 'previews', 'thought', 'american', 'sniper', 'didn', 'come', 'january', 'qecsmbgta', 'saw', 'american', 'sniper', 'movie', 'intense', 'going', 'see', 'american', 'sniper', 'ugbfaebi', 'americansniper', 'chris', 'kyle', 'widow', 'movie', 'kids', 'remember', 'dad', 'xoenmufuz', 'lftadfknt', 'post', 'got', 'right', 'american', 'sniper', 'great', 'movie', 'watchied', 'tell', 'someone', 'getting', 'paid', 'dickhead', 'saw', 'american', 'sniper', 'great', 'movie', 'thinking', 'soldiers', 'vets', 'families', 'mad', 'words', 'describe', 'sacrifice', 'way', 'beat', 'american', 'sniper', 'best', 'picture', 'characterize', 'people', 'like', 'nutjobs', 'hollywood', 'publicist', 'american', 'sniper', 'truly', 'great', 'learned', 'never', 'let', 'clint', 'surprise', 'expect', 'cry', 'credits', 'watch', 'american', 'sniper', 'week', 'old', 'son', 'proper', 'buzzing', 'loves', 'bradley', 'cooper', 'american', 'sniper', 'wins', 'box', 'office', 'ejqtqdlg', 'uzgbma', 'american', 'sniper', 'crazz', 'good', 'bradley', 'cooper', 'awesome', 'americansniper', 'nominated', 'bradley', 'cooper', 'fantastic', 'american', 'sniper', 'ditto', 'sienna', 'miller', 'american', 'sniper', 'widow', 'speechless', 'group', 'donates', 'proceeds', 'rifle', 'raffle', 'family', 'dczjvge', 'bawcxrxk', 'thought', 'american', 'sniper', 'didn', 'come', 'january', 'hgfcqulgk', 'armaniii', 'wesleystromberg', 'movie', 'going', 'see', 'sure', 'yet', 'really', 'wanna', 'see', 'american', 'sniper', 'haven', 'seen', 'american', 'sniper', 'correct', 'wrong', 'occupier', 'mows', 'faceless', 'iraqis', 'real', 'victim', 'anguished', 'soul', 'watch', 'americansniper', 'weekend', 'film', 'destroyed', 'several', 'box', 'office', 'records', 'mpumczzyg', 'wxegaaymix', 'american', 'sniper', 'feels', 'like', 'snorting', 'line', 'freedom', 'boner', 'founding', 'father', 'american', 'sniper', 'propaganda', 'film', 'azjbmqkmua', 'american', 'sniper', 'shatters', 'box', 'office', 'record', 'nationwide', 'opening', 'oipthfy', 'ojldkxzduj', 'thedaysofcontent', 'americansniper', 'jumqiorsef', 'retweet', 'going', 'see', 'american', 'sniper', 'utzacmelf']

def finding_topics(documents):
     texts = [[word for word in document.lower().split() if word not in stop] for document in documents]
     #print texts
     dictionary = corpora.Dictionary(texts)
     corpus = [dictionary.doc2bow(text) for text in texts]
     #print corpus

     lda = gensim.models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=1, update_every=1, chunksize=10000, passes=1)
#print lda.print_topics(5)

     topics_matrix = lda.show_topics(formatted=False, num_words=40)
     topics_matrix = np.array(topics_matrix)

     topic_words = topics_matrix[:,:,1]
     for i in topic_words:
         topic=([str(word) for word in i])
     return topic
