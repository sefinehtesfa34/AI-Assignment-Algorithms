import time
import pandas as pd 
import numpy as np 
from cmath import inf
import heapq 
from build_graph import instance_of_graph
from latitude_and_longitude import HeuristicGraphBuilder
class AStartAlgoritm:
    def shortest_path(self,graph, starting_vertex):
              
        self.distances = {vertex[1]: inf for vertex in graph}
        self.distances[starting_vertex[1]] = 0
        self.visited=set()
        self.heapped = [(starting_vertex)]
        self.path_tracker=[]
        self.solution_length=0
        self.total_distance=0
        while self.heapped:
            self.solution_length+=1
            self.heurstic,self.current_vertex = heapq.heappop(self.heapped)    
            
            self.total_distance+=self.heurstic
            
            self.visited.add(self.current_vertex)
            self.path_tracker.append(self.current_vertex)
            while self.heapped:
                top=heapq.heappop(self.heapped)
                self.visited.add(top[1])
                

            for neighbor, weight,heurstic in graph[(self.heurstic-self.distances[self.current_vertex],self.current_vertex)]:
                if neighbor in self.visited:continue
                if heurstic==0:
                    self.total_distance+=int(weight)+self.distances[self.current_vertex]
                    self.path_tracker.append(neighbor)
                    return 
                self.distance=int(weight)+self.distances[self.current_vertex]
                if self.distance < self.distances[neighbor]:
                    self.distances[neighbor] = self.distance
                heapq.heappush(self.heapped,(self.distances[neighbor]+heurstic,neighbor))
                

instance_for_Heurisitic_graph_builder=HeuristicGraphBuilder()                
#The target is on the latitude_and_longitude file
#Because we need to compute the heuristic function for each of cities from the target city
#Using the given latitude and longitude.
#If you want to change the target city, please go to the latitude_and _longitude file
#And change the target city with any city among the given cities
target="Eforie"
start_node="Oradea"

instance_for_AStar=AStartAlgoritm()

closeness_centerality={}
graph_for_nodes=instance_of_graph.graph
all_nodes=list(graph_for_nodes.keys())
for node in all_nodes:
    total=0
    for target in all_nodes:
        if node ==target:continue
        instance_for_Heurisitic_graph_builder.targe_initializer(target=target)
        instance_for_Heurisitic_graph_builder.heuristicGraphBuilder()
        distance=instance_for_Heurisitic_graph_builder.distance_from_node_to_target_node(node)
        graph=instance_for_Heurisitic_graph_builder.ready_heurstic_graph
        instance_for_AStar.shortest_path(graph,(distance,node))
        total+=instance_for_AStar.total_distance
    closeness_centerality[node]=(len(graph)-1)/total 


print("\n\tThe closeness centerality of all nodes using A* algorithm: \n")
# print(closeness_centerality)

df=pd.DataFrame(closeness_centerality.items(),columns=["City","ClosenessCenterality"])
print(df)
