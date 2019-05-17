# Python_NLP_Book
import nltk, re, pprint
from urllib import urlopen

if __name__ == '__main__':
	#raw语言数据需要包装成Text类
	raw = 'This is a test string.'
	tokens = nltk.word_tokenize(raw)
	text = nltk.Text(tokens)
	text.collocations()

	#读取本地文件
	path = nltk.data.find('corpora/gutenberg/melville-moby_dick.txt')
	raw = open(path, 'rU').read()

	#读取用户输出
	test = raw_input("Please type something...")
