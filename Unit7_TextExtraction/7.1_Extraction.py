# Python_NLP_Book
import nltk
from textwrap import fill

def ie_preprocess(document):
	sentences = nltk.sent_tokenize(document)
	sentences = [nltk.word_tokenize(sent) for sent in sentences]
	sentences = [nltk.pos_tag(sent) for sent in sentences]

if __name__ == '__main__':
	#From unstructured data to stuctured data
	