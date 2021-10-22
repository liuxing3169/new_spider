#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import Collection
import jieba
import os
from datetime import datetime
from wordcloud import WordCloud

# news_file_name = "logs/news/qq/" + datetime.now().strftime("%Y%m%d") + ".txt"
news_file_name = "logs/news/cnnews/" + datetime.now().strftime("%Y%m%d") + ".txt"
tmp_file = "logs/2.txt"

print(news_file_name)
newsfile = open(news_file_name, "r")
word_list = jieba.cut(newsfile.read())
if os.path.exists(tmp_file):
    os.remove(tmp_file)
f2 = open(tmp_file,"w")
f2.write(", ".join(word_list))
f2.close()
newsfile.close()

words = open(tmp_file, "r").read()

# Generate a word cloud image
font = r"font/simhei.ttf"
stopwords = {"好", "的", "年", "月", "在", "了", "和", "有", "副", "中", "是", "也", "等", "日", "你", "我", "他", "她", "不", "要", "不要", "对", "错", "否", "都","他们", "时","为", "被", "就", "到", "并", "又", "把", "或", "与", "但", "已", "后", "给", "该", "还"}
wordcloud = WordCloud(collocations=False, font_path=font, width=800, height=400, stopwords=stopwords ).generate(words)

# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

# # lower max_font_size
# wordcloud = WordCloud(max_font_size=40).generate(words)
# plt.figure()
# plt.imshow(wordcloud, interpolation="bilinear")
# plt.axis("off")
plt.show()

