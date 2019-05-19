# Python_NLP_Book
import nltk
from textwrap import fill

if __name__ == '__main__':
	#1.确定NE的边界 2.确定NE的类型
	sent = nltk.corpus.treebank.tagged_sents()[22]
	print(sent)

	#NLTK已经训练好的标注器
	#只考虑NE
	print(nltk.ne_chunk(sent, binary=True))
	#考虑PERSON,GPE,ORGANIZATION等
	print(nltk.ne_chunk(sent))
	