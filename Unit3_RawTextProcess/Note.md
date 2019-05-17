# 3.RawTextProcessing

3.1
-电子书

-HTML

-处理搜索引擎的结果
	*处理RSS订阅  帮助构建博客帖子的小语料库

-读取本地文件
	*open()/f.read()/for line in f: ...

-从二进制格式文件中读取数据
	*pypdf,pywin32

-获取用户输入
	raw_input("Some Hints..")

-NLP的流程
	HTML=>ASCII=>Text=>Words

3.2
pass

3.3
-import codecs
	*Python 的codecs 模块提供了将编码数据读入为Unicode 字符串和将Unicode 字符串以编码形式写出的函数。
	*f = codecs.open(path, encoding='latin2')/f_w = codecs.open(path, 'w', encoding='utf-8')

-ord('Char')
	*返回该字符的Unicode编码值

-print(u'\uXXXX')

3.4
-正则表达式 ^ $ ? + {x,y} [abc] [a-zA-Z] 

3.5
-正则表达式的用处 提取字符块/分析字符块/查找词干/搜索已分词文本

3.6
-词干提取器/词性归并
	*PorterStemmer()/LancasterStemmer()/WordNetLemmatizer()

3.7
-用正则表达式分词
	\b 词边界（零宽度）
	\d 任一十进制数字（相当于[0-9]）
	\D 任何非数字字符（等价于[^ 0-9]）
	\s 任何空白字符（相当于[ \t\n\r\f\v]）
	\S 任何非空白字符（相当于[^ \t\n\r\f\v]）
	\w 任何字母数字字符（相当于[a-zA-Z0-9_]）
	\W 任何非字母数字字符（相当于[^a-zA-Z0-9_]）
	\t 制表符
	\n 换行符
	*不同领域的分词器不同,通过访问原始文本会有帮助
3.8
-分割——断句/分词
	pass
3.9
-格式化:链表到字符串
