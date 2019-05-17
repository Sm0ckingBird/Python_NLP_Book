# Python_NLP_Book
import nltk, re, pprint

if __name__ == '__main__':
	#数据的定义
	raw = """'When I'M a Duchess,' she said to herself, (not in a very hopeful tone
	though), 'I won't have any pepper in my kitchen AT ALL. Soup does very
	well without--Maybe it's always pepper that makes people hot-tempered,'..."""
    
    #消除了制表符和换行符，仍然会出现(not的不友好案例
	print(re.split(r'[ \t\n]+', raw))
	#\W定义了数字字母的补集
	print(re.split(r'\W+', raw))
	#
	re.findall(r'\w+|\S\w*', raw)
	#
	re.findall(r"\w+(?:[-']\w+)*|'|[-.(]+|\S\w*", raw)

	#NLTK的正则表达式分词器
	text = 'That U.S.A. poster-print costs $12.40...'
	pattern = r'''(?x)
	([A-Z]\.)+
	| \w+(-\w+)*
	| \$?\d+(\.\d+)?%?
	| \.\.\.
	| [][.,;"'?():-_`]
	'''
	print(nltk.regexp_tokenize(text, pattern))