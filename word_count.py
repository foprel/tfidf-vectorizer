import re
from math import log
import os
import nltk
nltk.download('punkt')
from nltk import word_tokenize,sent_tokenize

corpus = """
This is a sentence. This is another sentence. There are three sentences.
"""

def preprocessing(doc):

	doc = re.sub("\n", " ", doc)
	doc = re.sub("[^A-Za-z0-9]+", " ", doc)
	doc = re.sub(" +", " ", doc)
	doc = doc.strip()
	doc = doc.lower()

	return(doc)

sentences = sent_tokenize(corpus)

dictionary  = {}

for sentence in sentences:
	dictionary[sentence] = {}

for sentence in dictionary:
	sentence = preprocessing(sentence)
	terms = word_tokenize(sentence)

	# lemmatize/stem terms
	
	for word_token in word_tokens:
		dictionary[sentence][word_token] = {}

print(dictionary)


# Split original text to sentences and add to dict
# Clean sentences, remove stopwords and split to list
# Lemmatize/stem terms
# Add words to dict
# Calculate tfidf per word
# Calculate tfidf-score per sentence
# Calculate treshold score (e.g. average score per sentence)
# Return all sentences above treshold


# docs = []

# for __, __, files in os.walk(os.getcwd(), topdown=False):
# 	for file in files:
# 		if ".txt" in file:
# 			f = open(file, "r")
# 			content = f.read()
# 			docs.append(content)



# def tokenize(doc):

# 	sentence = re.split('(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', doc)

# 	return(tokenized_sentences)



# def preprocessing(doc):

# 	doc = re.sub("\n", " ", doc)
# 	doc = re.sub("[^A-Za-z0-9]+", " ", doc)
# 	doc = re.sub(" +", " ", doc)
# 	doc = doc.strip()
# 	doc = doc.lower()

# 	return(doc)

# tfidf = {}


# def tf(terms):

# 	for term in terms:
# 		if term not in tfidf:
# 			tfidf[term] = {}
# 			tfidf[term]["termFrequency"] = 1
# 		elif term in tfidf:
# 			tfidf[term]["termFrequency"] += 1

# 	return

# def df(terms, docs):

# 	doc_list = []

# 	for doc in docs:
# 		doc = preprocessing(doc)
# 		doc_list.append(doc)

# 	for term in terms:
# 		tfidf[term]["docFrequency"] = 1
# 		for doc in docs:
# 			if term in doc:
# 				tfidf[term]["docFrequency"] += 1

# 	return

# def calc(tfidf):

# 	term_list = []

# 	for term in tfidf:
# 		tf = tfidf[term]["termFrequency"]
# 		doc_len = len(tfidf)
# 		df = tfidf[term]["docFrequency"]
# 		docs_len = len(docs)

# 		tfidf_calc = (tf/doc_len) * log(docs_len/df)

# 		term_list.append([tfidf_calc, term])

# 	results = sorted(term_list, reverse=True)[:10]

# 	print(results)