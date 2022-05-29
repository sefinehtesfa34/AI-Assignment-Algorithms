import time 
from cmath import inf
import heapq

import numpy as np
from build_graph import instance_of_graph
start=time.time()
class Dijkistra:
    def shortest_path(self,graph, starting_vertex,target):
        self.distances = {vertex: inf for vertex in graph}
        self.distances[starting_vertex] = 0
        self.visited=set()
        self.heapped = [(0, starting_vertex)]
        self.path_tracker={}
        self.solution_length=0
        while self.heapped:
            self.solution_length+=1
            self.current_distance, self.current_vertex = heapq.heappop(self.heapped)
            self.visited.add(self.current_vertex)
            if self.current_vertex==target:
                print("Inside the graph : ",self.solution_length)
                self.output=[]
                temp=self.current_vertex
                while temp!=starting_vertex:
                    self.output.insert(0,temp)
                    temp=self.path_tracker[temp]
                    
                self.output.insert(0,temp)
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
all_nodes=list(graph.keys())
solution_length=[]
time_taken=[]
for start_node in all_nodes:
    #We can convert a second into mili second by multiplying with 1000
    start_time=(time.time())*1000
    length=0
    for target_node in all_nodes:
        #If the start node is the target node, we don't need to compute a shortest distance.
        if start_node==target_node:continue        
        start=start_node
        target=target_node
        instance_for_Dijkistra.shortest_path(graph,start,target)
        length+=instance_for_Dijkistra.solution_length
        print("Outside the graph: ",instance_for_Dijkistra.solution_length)
        print(start,target)
        print(instance_for_Dijkistra.output)
    #We can change a second into milli second by multiplying with 1000
    end_time=(time.time())*1000
    solution_length.append(length/len(graph))    
    time_taken.append(end_time - start_time)
average_solution_length=np.sum(solution_length)/len(solution_length)
average_time_taken=np.sum(time_taken)/len(time_taken)
print("The average solution length for Dijkstra alogrithm: {} ".format(average_solution_length))
print("The average time taken for Dijkstra algorithm: {}".format(average_time_taken))
