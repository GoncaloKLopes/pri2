import nltk
import nltk.data
import re

from nltk.corpus import stopwords
from nltk.stem.porter import *
from wordsegment import load, segment

cachedStopWords = stopwords.words("english")

#returns array of sentences

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







#-----------------Not being used---------------------------#
def stem_sentence(sentence):
    stemmer = PorterStemmer()
    load()
    stemmed = ""
    sentence = segment(sentence)
    for word in sentence:
        stemmed += stemmer.stem(word) + ' '
    return stemmed

#returns list of sentences
def stem_text(text):
    text = re.sub("([a-zA-Z0-9])’[a-zA-Z0-9]",r'\1',text)
    sentences = text_to_sentences(text)
    stemmed = []
    for sentence in sentences:
        stemmed.append(stem_sentence(sentence))
    return stemmed

def remove_stopwords(text):
    return' '.join([word for word in text.split() if word not in cachedStopWords])