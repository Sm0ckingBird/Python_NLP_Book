# Python_NLP_Book
import nltk
from textwrap import fill

if __name__ == '__main__':
	#用级联分块器构建嵌套结构
	grammar = r"""
	NP: {<DT|JJ|NN.*>+} # Chunk sequences of DT, JJ, NN
	PP: {<IN><NP>} # Chunk prepositions followed by NP
	VP: {<VB.*><NP|PP|CLAUSE>+$} # Chunk verbs and their arguments
	CLAUSE: {<NP><VP>} # Chunk NP, VP
	"""

	cp = nltk.RegexpParser(grammar)

	sentence = [("Mary", "NN"), ("saw", "VBD"), ("the", "DT"), ("cat", "NN"),
	("sit", "VB"), ("on", "IN"), ("the", "DT"), ("mat", "NN")]
	print(cp.parse(sentence))

	#树的基本概念
	pass



	