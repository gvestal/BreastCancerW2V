'''
    Created on June 2017
    
    This script accompanies the data set released with the following publication:
    
    Sarker A, Gonzalez, G. A corpus for mining drug-related knowledge from Twitter chatter: Language models and their utilities. Data in Brief. 2016 Nov 23;10:122-131. eCollection 2017 Feb.
    
    In the paper, small models are discussed and presented for system development. This is an extension.
    The model was generated with ~1 billion tweets involving drug-relted chatter, or from the profiles of users involved in drug-related chatter. All the tweets were collected using the Twitter public streaming API.
    
    This model is a n-gram model. To express multi-word expressions, please use the underscore character (e.g., new_york, high_blood_pressure).
    
    The model is in word2vec C format.
    
    The script shows how the DSM langauge model can be loaded and sample operations.
    
    Author: Abeed Sarker
    Email: abeed@upenn.edu
    
    Prerequisite: gensim
    
    @author: asarker
    '''
from gensim.models import Word2Vec
filename = 'trig-vectors-phrase.bin'
print 'loading model this may take a while'
model = Word2Vec.load_word2vec_format(filename, binary=True, encoding='utf8',unicode_errors='ignore')

print model.most_similar("paxil")
print model.most_similar("adderall")
print model.most_similar("headache")


