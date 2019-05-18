# Python_NLP_Book
import nltk
from textwrap import fill

if __name__ == '__main__':
	#表示已标注的标识符
	tagged_token = nltk.tag.str2tuple('fly/NN')
	print(tagged_token)

	#读取已标注的语料库,simiplify以使用简单标签
	temp = nltk.corpus.brown.tagged_words(tagset='universal')
	print(temp[:10])

	#简化的词性标记集
	brown_news_tagged = nltk.corpus.brown.tagged_words(categories='news',tagset='universal')
	tag_fd = nltk.FreqDist(tag for (word, tag) in brown_news_tagged)
	for item in tag_fd.keys():
		print("{}:{}".format(item,tag_fd[item]))

	#名词
	word_tag_pairs = nltk.bigrams(brown_news_tagged)
	print(dict(nltk.FreqDist(a[1] for (a, b) in word_tag_pairs if b[1] == 'NOUN')))

	#动词
	wsj = nltk.corpus.treebank.tagged_words(tagset='universal')
	word_tag_fd = nltk.FreqDist(wsj)

	cfd1 = nltk.ConditionalFreqDist(wsj)
	print(cfd1['yield'].keys())
	cfd2 = nltk.ConditionalFreqDist((tag, word) for (word, tag) in wsj)
	print(cfd2['VN'].keys())

	#形容词和副词
	pass

	#未简化的标记
	pass

	#已标注的语料库
	brown_learned_text = brown.words(categories='learned')
