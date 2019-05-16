# Python_NLP_Book
import nltk
from nltk.corpus import stopwords
from nltk.corpus import swadesh

#词汇列表语料库
def unusual_words(text):
	text_vocab = set(w.lower() for w in text if w.isalpha())
	english_vocab = set(w.lower() for w in nltk.corpus.words.words())
	unusual = text_vocab.difference(english_vocab)
	return sorted(unusual)

#停用词
def StopWords(length):
	temp = stopwords.words("english")
	return temp[:length]

def content_fraction(text):
	temp = stopwords.words("english")
	content = [w for w in text if w not in temp]
	return len(content)/len(text)

def difference(text):
	return set(text).difference(stopwords.words("english"))

#名字词典
def name_dict():
	names = nltk.corpus.names
	cfd = nltk.ConditionalFreqDist(
		(fileid, name[-1])
		for fileid in names.fileids()
		for name in names.words(fileid))
	choice = ['a','b','c','d','e']
	gender = ['female','male']
	cfd.tabulate(samples = choice)

#发音词典 CMU_DICT
def phonetic_dict():
	entries = nltk.corpus.cmudict.entries()
	for entry in entries[30000:30005]:
		print(entry)

#比较词表
def transformation():
	fr2en = swadesh.entries(['fr', 'en'])
	translate = dict(fr2en)
	print("chien => {}".format(translate['chien']))
	print("jeter => {}".format(translate['jeter']))
	languages = ['en', 'de', 'nl', 'es', 'fr', 'pt']
	for i in [139, 140, 141, 142]:
		print(swadesh.entries(languages)[i])


if __name__ == '__main__':
	#展示不常见的单词
	print("Unusual words in austen-sense text:")
	print(unusual_words(nltk.corpus.gutenberg.words('austen-sense.txt'))[:5])
	#展示部分停用词
	print("-----------------------------------------------------------------")
	print("StopWords[:5]\n{}".format(StopWords(5)))
	#展示除了停用词的词汇的比例
	print("-----------------------------------------------------------------")
	print("Percent of meaningful words in austen-sense text:")
	print(content_fraction(nltk.corpus.gutenberg.words('austen-sense.txt')))
	#展示名字的特性
	print("-----------------------------------------------------------------")
	name_dict()
	#展示发音词典
	print("-----------------------------------------------------------------")
	phonetic_dict()
	#展示比较词表
	print("-----------------------------------------------------------------")
	transformation()
