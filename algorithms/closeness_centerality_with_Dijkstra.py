import pandas as pd 
import time 
from cmath import inf
import heapq
from turtle import distance
from build_graph import instance_of_graph
start=time.time()
class Dijkistra:
    def shortest_path(self,graph, starting_vertex,target):
        self.distances = {vertex: inf for vertex in graph}
        self.distances[starting_vertex] = 0
        self.visited=set()
        self.heapped = [(0, starting_vertex)]
        self.path_tracker={}
        while self.heapped:
            self.current_distance, self.current_vertex = heapq.heappop(self.heapped)
            self.visited.add(self.current_vertex)
            if self.current_vertex==target:
                return 
            
            for neighbor, weight in graph[self.current_vertex].items():
                if neighbor in self.visited:continue
                self.distance = self.current_distance + int(weight)
                if self.distance < self.distances[neighbor]:
                    self.distances[neighbor] = self.distance
                    self.path_tracker[neighbor]=self.current_vertex
                    heapq.heappush(self.heapped, (self.distance, neighbor))
graph=instance_of_graph.graph
for key in graph:
    graph[key]=dict(graph[key])
instance_for_Dijkistra=Dijkistra()
closeness_centerality={}
for node in graph:
    total=0
    for target in graph:
        if node==target:continue
        instance_for_Dijkistra.shortest_path(graph,node,target)
        distance=instance_for_Dijkistra.current_distance
        total+=distance
    closeness_centerality[node]=(len(graph)-1)/total 

print("\n\tThe closeness centerality of all nodes using Dijkstra algorithm: \n")
# print(closeness_centerality)

df=pd.DataFrame(closeness_centerality.items(),columns=["City","ClosenessCenterality"])
print(df)
