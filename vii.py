# -*- coding: utf-8 -*-
"""vii.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10mdjQghbbzU8x8K5UnsQ4V87oDvNeYwV
"""

# 방향 그래프, 멀티 그래프

# 연결 중심성, 근접 중심성, 매개 중심성, 고유벡터 중심성



import networkx as nx
import matplotlib.pyplot as plt

borders = nx.Graph()
not_borders1 = nx.DiGraph()
not_borders2 = nx.MultiGraph()

borders = nx.read_graphml('borders-1.graphml')

borders.add_node("Zimbabwe")
borders.add_nodes_from(["Lugandon", "Zambia", "Portugal", "Kuwait", "Colombia"])
borders.remove_node("Lugandon")
borders.add_edge("Zambia", "Zimbabwe")
borders.add_edges_from([("Uganda", "Rwanda"), ("Uganda", "Kenya"), ("Uganda", "South Sudan"), ("Uganda", "Tanzania"), ("Uganda", "Democratic Republic of the Congo")])

# clear()

len(borders)

borders.nodes() #node

borders.node # node의 속성

borders.edge # 노드의 개수만큼 있는 딕셔너리들의 딕셔너리 반환

borders.edges()[:5]

borders.neighbors("Germany") # 노트에 이웃한 노드 리스트

borders.degree("Poland")

borders.degree()

import pandas
degrees = pandas.DataFrame(list(borders.degree().items()), columns=("country","degree")).set_index("country")
degrees.sort("degree").tail(4)

nx.clustering(nx.Graph(not_borders1)) # 방향그래프에서는 작동 x

nx.clustering(borders)

nx.clustering(borders, "Lithuania") # 미작동

list(nx.connected_components(borders)

[len(x) for x in nx.connected_component_subgraphs(borders)]

nx.degree_centrality(borders)
nx.in_degree_centrality(borders)
nx.out_degree_centrality(borders)
nx.closeness_centrality(borders)
nx.betweennes_centrality(borders)
nx.engenvector_centrality(borders)

borders.nodes(data=True)

borders.edges(data=True)

nx.find_cliques(not_borders1)) # 방향 그래프에서 사용 불가능

nx.find_cliques(nx.Graph(not_borders1))
list(nx.find_cliques(borders))

nx.isolates(borders)

import community
partition = community.best_partition(borders)
partition

community.modularity(partition, borders)

with open ("borders-1.graphml", "wb") as netfile:
  nx.write_pajek(borders, netfile)
with open ("file.net", "rb") as netfile:
  borders = nx.read_pajek(netfile)


