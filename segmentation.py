

from LAC import LAC

# 装载LAC模型
lac = LAC(mode='seg')

# 装载干预词典, sep参数表示词典文件采用的分隔符，为None时默认使用空格或制表符'\t'
lac.load_customization('custom.txt', sep=None)

# 批量样本输入, 输入为多个句子组成的list，平均速率会更快
texts = [u"LAC是个优秀的分词工具", u"百度是一家高科技公司"]
seg_result = lac.run(texts)
print(seg_result)

with open('诡秘之主.txt', 'r') as a:
    lines = a.read().split('\n')
    seg_result = lac.run(lines)

with open('诡秘之主_分词.txt','a+') as b:
    for i in seg_result:
        b.write(' '.join(i)+"\n")