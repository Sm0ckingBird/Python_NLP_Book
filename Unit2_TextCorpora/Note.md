# 2.TextCorpora

Emma = nltk.Text(list)       以获得NLTK中的text对象
cfd = nltk.ConditionalFreqDist(
... (genre, word)
... for genre in brown.categories()
... for word in brown.words(categories=genre))
—带条件的频率分布
cfd.tabulate(conditions=genres, samples=modals)

构建自己的语料库