# # s1 = "hello my intra id is jaeyyoo"
# # p = s1.split(' ')

# # s2 = "hello      ,my     ,name  ,is ,jaeyeong!!!"
# # p2 = [x.strip(' ') for x in s2.split(',')]


# # w1 = 'aaa'
# # w2 = 'really'
# # w3 = 'boring'
# # p3 = ' '.join([w1, w2, w3])

# # p4 = p3.replace(' ', '~~')

# # p5 = p4.upper()

# # p6 = p5.capitalize()

# # p7 = p6.find('o')

# # print(p,'\n',p2,'\n',p3,'\n',p4,'\n',p5,'\n',p6,'\n',p7)

# # import wikipedia as wp
# # from wordcloud import WordCloud, STOPWORDS
# # import matplotlib.pyplot as plt

# # wiki = wp.page('korea')
# # text = wiki.content

# # s_word = STOPWORDS.union({'one', 'using', 'first', 'two'})
# # wordcloud = WordCloud(width=200, height=150, stopwords=s_word).generate(text)

# # plt.figure(figsize=(40,30))
# # plt.imshow(wordcloud)
# # plt.show()

# import re

# print(re.search('AB*', 'CABBBABA'))
# print(re.search('AB?', 'CABBBABA'))


import re
txt1 = 'Life is too short, you need good life'
txt2 = 'The best momente of my life'

match = re.search('[Ll]ife', txt1)
print(match.group())