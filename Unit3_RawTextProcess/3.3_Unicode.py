# Python_NLP_Book
import nltk, re, pprint
import codecs
import sys


if __name__ == '__main__':
	path = nltk.data.find('corpora/unicode_samples/polish-lat2.txt')
	f = codecs.open(path, encoding='latin2')
	#f_w = codecs.open(path, 'w', encoding='utf-8')
	you = u'\u4f60'
	you_utf = you.encode('utf8')
	print(you_utf)
