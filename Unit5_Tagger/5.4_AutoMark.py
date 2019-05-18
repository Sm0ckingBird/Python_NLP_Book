# Python_NLP_Book
import nltk
from textwrap import fill
from nltk.corpus import brown

if __name__ == '__main__':
	#我们需要处理句子层次而不是词汇层次的数据
	brown_tagged_sents = brown.tagged_sents(categories='news')
	brown_sents = brown.sents(categories='news')

	#默认标注器-benchmark
	tags = [tag for (word, tag) in brown.tagged_words(categories='news')]
	print(nltk.FreqDist(tags).max())
	#由此得出名词出现的概率最大
	default_tagger = nltk.DefaultTagger('NN')
	print(default_tagger.evaluate(brown_tagged_sents))

	#正则表达式标注器
	patterns = [
	(r'.*ing$', 'VBG'), # gerunds
	(r'.*ed$', 'VBD'), # simple past
	(r'.*es$', 'VBZ'), # 3rd singular present
	(r'.*ould$', 'MD'), # modals
	(r'.*\'s$', 'NN$'), # possessive nouns
	(r'.*s$', 'NNS'), # plural nouns
	(r'^-?[0-9]+(.[0-9]+)?$', 'CD'), # cardinal numbers
	(r'.*', 'NN') # nouns (default)
	]

	regexp_tagger = nltk.RegexpTagger(patterns)
	print(regexp_tagger.tag(brown_sents[3]))
	print(regexp_tagger.evaluate(brown_tagged_sents))

	#查询标注器
	fd = nltk.FreqDist(brown.words(categories='news'))
	cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))
	most_freq_words = fd.keys()[:100]
	likely_tags = dict((word, cfd[word].max()) for word in most_freq_words)
	baseline_tagger = nltk.UnigramTagger(model=likely_tags)
	print(baseline_tagger.evaluate(brown_tagged_sents))

	#回退操作,在一个标注器中无法标注,则使用下一个标注器
	baseline_tagger = nltk.UnigramTagger(model=likely_tags,
	backoff=nltk.DefaultTagger('NN'))

	#评估
	#可以使用黄金标准测试数据来评判标注器的优劣
