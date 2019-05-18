# Python_NLP_Book
import nltk

if __name__ == '__main__':
	#使用词性标注器
	text = nltk.word_tokenize("I will process it.")
	print(nltk.pos_tag(text))

	#从上下文获取信息
	text = nltk.Text(word.lower() for word in nltk.corpus.brown.words())
	text.similar('woman')
	text.common_contexts(['woman','man'])
