# Python_NLP_Book
import nltk, re, pprint

if __name__ == '__main__':
	#数据的定义
	raw = """DENNIS: Listen, strange women lying in ponds distributing swords
    is no basis for a system of government. Supreme executive power derives from
    a mandate from the masses, not from some farcical aquatic ceremony."""

    tokens = nltk.word_tokenize(raw)
    #nltk自带词干提取器
    porter = nltk.PorterStemmer()
    lancaster = nltk.LancasterStemmer()
    print([porter.stem(t) for t in tokens])
    print([lancaster.stem(i) for i in tokens])

    #词形归并 比词干提取器更加精准,会在自己的字典中查询
    wnl = nltk.WordNetLemmatizer()
	print([wnl.lemmatize(t) for t in tokens])