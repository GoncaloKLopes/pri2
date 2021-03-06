import nltk
import nltk.data
import re
import numpy as np

from nltk.corpus import stopwords
from nltk.stem.porter import *
from wordsegment import load, segment
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import priors

cachedStopWords = nltk.corpus.stopwords.words('portuguese')
#nltk.download('rslp')
#returns array of sentences
def text_to_sentences(text):
	text = re.sub('(\w)(\\n)+', r'\1. ',text)
	tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

	text = '\n-----\n'.join(tokenizer.tokenize(text))
	return text.split('\n-----\n')


#both args are text
def AP(systemSummaries, targetSummaries):
	systemSents = text_to_sentences(systemSummaries)
	targetSents = text_to_sentences(targetSummaries)

	AP = 0
	positives = 0
	total = 0
	for sent in systemSents:
		total += 1
		if sent in targetSents:
			positives += 1
			AP += positives/ total
	return AP/len(targetSents)

#sentences is a list, returns cossim matrix
def get_cosine_similarities_matrix(sentences):	
	vec = TfidfVectorizer()#stop_words=cachedStopWords)


	X = vec.fit_transform(sentences)
	return cosine_similarity(X)

#receives cossim matrix for performance reasons
#receives indexes for performance reasons aswell...
#also doubles as a weight, ignore t and sentences
def cos_sim(sent1_index,sent2_index,cosine_matrix):
    return cosine_matrix[sent1_index][sent2_index]

def degree_centrality(sent_index,sentences,t=0.2):
	graph = build_graph_uniform(sentences,t)
	return priors.degree_centrality_prior(sent_index,graph,sentences)






#--------------------------graph building stuff------------------------#
def build_graph_uniform(sentences,t=0.2):
    nsents = len(sentences)
    weights = np.zeros([nsents,nsents])
    cos_matrix = get_cosine_similarities_matrix(sentences)
    #create weights
    for i in range(len(sentences)):
        for j in range(len(sentences)):
            weights[i][j] = (cos_sim(i,j,cos_matrix) >= t) and (i != j)
    return weights




#-----------------Not being used---------------------------#
def stem_sentence(sentence):
    stemmer = nltk.stem.RSLPStemmer()
    load()
    stemmed = ""
    sentence = segment(sentence)
    for word in sentence:
        stemmed += stemmer.stem(word) + ' '
    return stemmed

#returns list of sentences
def stem_text(text):
    #text = re.sub("([a-zA-Z0-9])’[a-zA-Z0-9]",r'\1',text)
    sentences = text_to_sentences(text)
    stemmed = []
    for sentence in sentences:
        stemmed.append(stem_sentence(sentence))
    return stemmed

def remove_stopwords(text):
    return' '.join([word for word in text.split() if word not in cachedStopWords])
