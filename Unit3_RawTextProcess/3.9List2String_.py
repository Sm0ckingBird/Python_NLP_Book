# Python_NLP_Book
import nltk, re, pprint
from textwrap import fill

if __name__ == '__main__':
	silly = ['We', 'called', 'him', 'Tortoise', 'because', 'he', 'taught', 'us', '.']
	#' '被称作胶水词
	print(' '.join(silly))
	#格式化输出
	fdist = nltk.FreqDist(['dog', 'cat', 'dog', 'cat', 'dog', 'snake', 'dog', 'cat'])
	for word in fdist:
		print('%s->%d;' % (word, fdist[word]))
	#对齐fangshi
	#右对齐
	print('%6s' % 'dog')
	#左对齐
	print('%-6s' % 'dog')

	#将结果写入文件
	#output_file.write(word + "\n")

	#使用fill保证行不溢出
	#wrapped = fill(output)
	#print(wrapped)

