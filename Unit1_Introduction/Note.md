# 1.Introduction

-搜索文本 		concordance(word)/similar(word)/common_contexts(list)

-计数词汇 		len(text)/set(text)/text.count(word)

-将文本当作词链表 	list的基本操作

-频率分布 		FreqDist(text) return dict; word: 次数

-细粒度选词 		sorted([w for w in set(text) if len(w) > 7 and fdist[w] > 7])

-词语搭配和双连词	bigrams(list) return bi_list;  text.collocations() show bigrams;

-决策与控制	