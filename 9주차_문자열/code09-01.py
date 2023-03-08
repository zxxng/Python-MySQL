import wikipedia as wp
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

wiki = wp.page('korea')
wiki2 = wp.page('japan')
text = wiki.content + wiki2.content

# wordcloud = WordCloud(width = 2000, height = 1500).generate(text)

s_word = STOPWORDS.union({'south', 'north', 'korea', 'world', 'country'})
wordcloud = WordCloud(width = 2000, height = 1500, stopwords = s_word).generate(text)


plt.figure(figsize=(40,30))
plt.imshow(wordcloud)
plt.show()