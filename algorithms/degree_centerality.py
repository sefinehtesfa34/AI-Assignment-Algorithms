import pandas as pd 
from build_graph import instance_of_graph
graph=instance_of_graph.graph
degree_centerality={}
for node in graph:
    degree=len(graph[node])/(len(graph)-1)
    degree_centerality[node]=degree 
print("\nDegree Centerality\n")
df=pd.DataFrame(degree_centerality.items(),columns=["City","DegreeCenterality"])
print(df)

