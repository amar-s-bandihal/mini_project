import numpy as np 
import pandas as pd
import igraph
import matplotlib.pyplot as plt
import math


import networkx as nx
import os
for dirname, _, filenames in os.walk('E:\\project\\data set'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
        
import pandas as pd 
# #twitter
twitter = pd.read_excel("E:\\project\\data set\\Twitter_Data.xlsx", sheet_name = "Sheet1")
twitter2 = twitter[twitter.columns[1:17]]
twitter3 = twitter2.head(n=16)
twitter4=twitter3.to_numpy()
graph = igraph.Graph.Adjacency(twitter4.astype(bool).tolist())


# #  Facebook
facebook =pd.read_excel("E:\\project\\data set\\Facebook_Data.xlsx",sheet_name="Sheet1")
facebook2 = facebook[facebook.columns[1:17]]
facebook3 = facebook2.head(n=16)
facebook4=facebook3.to_numpy()
graph = igraph.Graph.Adjacency(facebook4.astype(bool).tolist())

# #instagram
instagram =pd.read_excel("E:\\project\\data set\\Instagram_Data.xlsx",sheet_name="Sheet1")
instagram2 = instagram[instagram.columns[1:17]]
instagram3 = instagram2.head(n=16)
instagram4=instagram3.to_numpy()
graph = igraph.Graph.Adjacency(instagram4.astype(bool).tolist())

igraph.plot(graph, layout = 'circle')
print(graph.density()/2)
print(graph.density())
print(graph.density(loops = True ))
print(max(graph.indegree()))
print(max(graph.outdegree()))
c=graph.edge_betweenness()
print(twitter.iloc[c.index(max(c))][0])
print(str(c.index(max(c))) + ", " + str(max(c)))
o=graph.pagerank()
print(twitter.iloc[o.index(max(o))][0])
print(str(o.index(max(o))) + ", " + str(max(o)))
# graph.is_directed()
# dg = graph.degree() 
# plt.hist(dg, bins=25)