# Python_NLP_Book
import nltk, re, pprint

if __name__ == '__main__':
	#整个单词表
	wordlist = [w for w in nltk.corpus.words.words('en') if w.islower()]
	print(wordlist[1000:1010])
	#以ed结尾的单词
	list_ed = [w for w in wordlist if re.search('ed$', w)]
	print(list_ed[:10])
	#XXjXXtXX
	list_myth = [w for w in wordlist if re.search('^..j..t..$', w)]
	print(list_myth)
	#计算email/e-mail出现的总次数
	text = ['email','e-mail','see','mother']
	print(sum(1 for w in text if re.search('^e-?mail$', w)))
	#在字符串前加r表示是原始字符串，不转义
	#r'\band\b'  \b表示退格
	