# novel_nlp
tfidf关键字提取，使用lac分词  
目前测试了诡秘之主

修改了TfidfVectorizer里边的一个地方，即
```
idf = np.log(n_samples / df)
改为
idf = np.log(n_samples / df)/np.log(1.1) + 1
```
修改调参了log的底数/基数  
使得idf 逆向文件频率 逆向文档频率 的权重增加  
目前为1.1，越接近1，idf权重越大  

如果完全去掉np.log，idf的权重就太大了，还是不要去掉

一开始是用的乘，发现乘不行，得改log的底数/基数

