# Python_NLP_Book
import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords


def RecognitionOfEntity(words):
	result = dict()
	for item in words:
		temp = []
		sets = wn.synsets(item)
		for s in sets:
			temp.append(s.root_hypernyms())
		result[item] = temp
	return result



if __name__ == '__main__':
	#motorcar属于的同义词集
	print(wn.synsets('motorcar'))
	#属于car.n.01同意词集的所有单词
	print(wn.synset('car.n.01').lemma_names())
	#car.n.01的定义
	print(wn.synset('car.n.01').definition())
	#car.n.01的例句
	print(wn.synset('car.n.01').examples())
	#car.n.01的词元
	print(wn.synset('car.n.01').lemmas())
	#car.n.01的automobile词元
	print(wn.lemma('car.n.01.automobile'))
	#car.n.01的automobile词元所属的集合
	print(wn.lemma('car.n.01.automobile').synset())
	#car.n.01的automobile词元的名称
	print(wn.lemma('car.n.01.automobile').name())

	#模糊词car
	for synset in wn.synsets('car'):
		print(synset.lemma_names())

	#WordNet的网状结构
	motorcar = wn.synset('car.n.01')
	#下位词
	types_of_motorcar = motorcar.hyponyms()
	print(sorted([lemma.name() for synset in types_of_motorcar for lemma in synset.lemmas()]))

	#上位词
	#上一层
	print(motorcar.hypernyms())
	paths = motorcar.hypernym_paths()
	print([synset.name() for synset in paths[0]])
	print([synset.name() for synset in paths[1]])
	#最普通的一层
	print(motorcar.root_hypernyms())

	#我的Test, 在DNA甲基化论文上找了一个句子
	words = str.split("DNA methylation is a crucial epigenetic modification of the genome that is involved regulating many cellular processes")
	feature_words = set(words).difference(stopwords.words("english"))
	print(RecognitionOfEntity(feature_words))

	#更多的词汇关系 上位和下位是同义集的关系 还有整体和部分的关系
	#部分关系 树的部分树干,树冠
	print(wn.synset('tree.n.01').part_meronyms())
	#实质关系 树的实质心材,边材
	print(wn.synset('tree.n.01').substance_meronyms())
	#整体关系 树木构成森林
	print(wn.synset('tree.n.01').member_holonyms())
	#蕴含关系 走路蕴含抬脚
	print(wn.synset('walk.v.01').entailments())
	#反义词
	print(wn.lemma('horizontal.a.01.horizontal').antonyms())
	#其他词汇关系
	print(dir(wn.synset('harmony.n.02')))

	#语义相似度
	right = wn.synset('right_whale.n.01')
	minke = wn.synset('minke_whale.n.01')
	print(right.lowest_common_hypernyms(minke))
	print(wn.synset('whale.n.02').min_depth())
	print(right.path_similarity(minke))
