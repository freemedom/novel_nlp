import re
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
# corpus = [
#     'Thi is the firs document.',
#     'This document is the second document.',
#     'And this is the third one.',
#     'Is this the first document?',
# ]

with open('诡秘之主_分词.txt', 'r') as a:
    lines = a.read()
corpus = re.split('\n(?=第\d)',lines)
# print(1)

#
with open('诡秘之主.txt', 'r') as a:
    lines = a.read()
titles=re.findall('第\d+章.+',lines)
titles += [''] * (len(corpus) - len(titles))

#
stop_words_file = r"stopwordsHIT.txt"
stopwords = open(stop_words_file, encoding='utf-8').read()
stopwords = stopwords.split()


#
max_df=0.5
vectorizer = TfidfVectorizer(token_pattern=u'(?u)\\b[\u4e00-\u9fa5]\\w+\\b',
                             #默认为token_pattern=r"(?u)\b\w\w+\b",
                             stop_words=stopwords,
                             max_df = max_df)
X = vectorizer.fit_transform(corpus)
# print(vectorizer.get_feature_names_out())
# print(vectorizer.vocabulary_)

# print(X.todense())# csr_matrix scipy.sparse.csr_matrix
# print(X.toarray())
# print(X.shape)


feature_names = np.array(vectorizer.get_feature_names())


def get_top_tf_idf_words(response, top_n):
    sorted_nzs = np.argsort(response.data)[:-(top_n + 1):-1]
    return feature_names[response.indices[sorted_nzs]]


res = [list(get_top_tf_idf_words(response, 10)) for response in X]
# for i in res:
#     print(i)

import pandas as pd
def write_csv(datalist,path):
    test=pd.DataFrame(data=datalist,index=titles)
    test.to_csv(path, encoding='gbk',header=False)#,index=False
    return test
write_csv(res,'改log关键词'+str(max_df)+'.csv')
