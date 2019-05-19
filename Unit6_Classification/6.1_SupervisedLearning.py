# Python_NLP_Book
import nltk
from textwrap import fill
from nltk.corpus import names
import random

#性别鉴定
def gender_features(word):
	return {'last_letter': word[-1]}

#根据Error分析，选择更好的特征
def gender_features2(name):
	features = {}
	features["firstletter"] = name[0].lower()
	features["lastletter"] = name[-1].lower()
	for letter in 'abcdefghijklmnopqrstuvwxyz':
		features["count(%s)" % letter] = name.lower().count(letter)
		features["has(%s)" % letter] = (letter in name.lower())
	return features

if __name__ == '__main__':
	#文档分类
	pass

	#上下文分类
	#将上下文的信息作为特征之一
	pass

	#序列分类

	#其他序列分类,HMM/CRF

	
