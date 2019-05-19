# Python_NLP_Book
import nltk
from textwrap import fill

if __name__ == '__main__':
	#标记模式
	sentence = [("the", "DT"), ("little", "JJ"), ("yellow", "JJ"),
	("dog", "NN"), ("barked", "VBD"), ("at", "IN"), ("the", "DT"), ("cat", "NN")]
	grammar = "NP: {<DT>?<JJ>*<NN>}"
	cp = nltk.RegexpParser(grammar)
	result = cp.parse(sentence)
	print(result)

	#探索文本语料库
	cp = nltk.RegexpParser('CHUNK: {<V.*> <TO> <V.*>}')
	brown = nltk.corpus.brown
	for sent in brown.tagged_sents():
		tree = cp.parse(sent)
		for subtree in tree.subtrees():
			if subtree.node == 'CHUNK': print(subtree)

	#加缝隙
	grammar = r"""
	NP:
	{<.*>+} # Chunk everything
	}<VBD|IN>+{ # Chink sequences of VBD and IN
	"""
	sentence = [("the", "DT"), ("little", "JJ"), ("yellow", "JJ"),
	("dog", "NN"), ("barked", "VBD"), ("at", "IN"), ("the", "DT"), ("cat", "NN")]
	cp = nltk.RegexpParser(grammar)
	print(cp.parse(sentence))

	#使用IOB表示块/NLTK内部使用树表示块








	