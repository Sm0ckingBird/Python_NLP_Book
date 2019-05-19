# Python_NLP_Book
import nltk
from textwrap import fill

if __name__ == '__main__':
	#IOB格式的语料库
	from nltk.corpus import conll2000
	print(conll2000.chunked_sents('train.txt')[99])
	#只查看NP类型的块
	print(conll2000.chunked_sents('train.txt', chunk_types=['NP'])[99])
	
	#简单评估和基准-基准模型
	cp = nltk.RegexpParser("")
	test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])
	print(cp.evaluate(test_sents))

	#正则表达式分块器
	grammar = r"NP: {<[CDJNP].*>+}"
	cp = nltk.RegexpParser(grammar)
	print(cp.evaluate(test_sents))

	#Unigram Chunker/Bigram Chunker
	pass

	#基于分类器的分块器/原理类比于N-gram，包含了前面的信息





	