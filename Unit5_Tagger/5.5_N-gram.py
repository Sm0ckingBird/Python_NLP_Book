# Python_NLP_Book
import nltk
from nltk.corpus import brown

if __name__ == '__main__':
	#一元标注
	brown_tagged_sents = brown.tagged_sents(categories='news')
	brown_sents = brown.sents(categories='news')
	unigram_tagger = nltk.UnigramTagger(brown_tagged_sents)
	unigram_tagger.evaluate(brown_tagged_sents)

	#分离数据
	size = int(len(brown_tagged_sents) * 0.9)
	train_sents = brown_tagged_sents[:size]
	test_sents = brown_tagged_sents[size:]
	unigram_tagger = nltk.UnigramTagger(train_sents)
	unigram_tagger.evaluate(test_sents)

	#N-gram标注/2-gram
	bigram_tagger = nltk.BigramTagger(train_sents)
	bigram_tagger.tag(brown_sents[2007])
	bigram_tagger.tag(unseen_sent)
	bigram_tagger.evaluate(test_sents)

	#组合标注器
	t0 = nltk.DefaultTagger('NN')
	t1 = nltk.UnigramTagger(train_sents, backoff=t0)
	t2 = nltk.BigramTagger(train_sents, backoff=t1)
	t2.evaluate(test_sents)

	#标注生词/用‘UNK’代替生词

	#存储标注器
	from cPickle import dump
	output = open('t2.pkl', 'wb')
	dump(t2, output, -1)
	output.close()

	from cPickle import load
	input = open('t2.pkl', 'rb')
	tagger = load(input)
	input.close()






