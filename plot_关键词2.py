import networkx as nx
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False



# G = nx.Graph()
# G.add_node('周明瑞')
# G.add_node('阿尔杰')
# G.add_node('周明瑞')
# G.add_node('阿尔杰')

#
# #nx.circular_layout(G)
# nx.draw(G, pos=nx.shell_layout(G),
#         with_labels=True,
#        )
# plt.show()

# G_karate = nx.read_gml('temp.gml')
# print(G_karate)
# nx.draw(G_karate, with_labels=True)
# plt.show()
import pandas as pd
df=pd.read_csv("绘制_test.csv",encoding='gbk', header=None)

list_df=df.iloc[:,1:].values.tolist()

# user_input = "aaaaabbbbcccdde"
# i is the node identifier and l is its corresponding label:
list_df=[i for j in list_df for i in j]

labels = {i: l for i, l in enumerate(list_df)}
# nodes = labels.keys()


left, right, bottom, top, layer_sizes = .1, .9, .1, .9, [10]*int((len(list_df)/10))
# 网络离上下左右的距离
# layter_sizes可以自己调整
import random
G = nx.Graph()
v_spacing = (top - bottom)/float(max(layer_sizes))
h_spacing = (right - left)/float(len(layer_sizes) - 1)
node_count = 0
for i, v in enumerate(layer_sizes):
    layer_top = v_spacing*(v-1)/2. + (top + bottom)/2.
    for j in range(v):
        G.add_node(node_count, pos=(left + i*h_spacing, layer_top - j*v_spacing))
        node_count += 1

for x, (left_nodes, right_nodes) in enumerate(zip(layer_sizes[:-1], layer_sizes[1:])):
    for i in range(left_nodes):
        for j in range(right_nodes):
            id_left = i + sum(layer_sizes[:x])
            id_right = j + sum(layer_sizes[:x + 1])
            if(labels[id_left]==labels[id_right]):
                G.add_edge(id_left, id_right)

#
# G = nx.DiGraph()
# G.add_nodes_from(nodes)

# pos = nx.spring_layout(G)
# pos=nx.circular_layout(G)
pos=nx.get_node_attributes(G,'pos')# 把每个节点中的位置pos信息导出来

plt.figure(figsize=(60, 10))
nx.draw(G, pos,node_color='white')
nx.draw_networkx_labels(G, pos, labels)
plt.savefig("关键词.png")
# plt.show()