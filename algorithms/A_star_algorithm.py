import time
import numpy as np 
from cmath import inf
import heapq 
from latitude_and_longitude import HeuristicGraphBuilder
from build_graph import instance_of_graph
class AStartAlgoritm:
    def shortest_path(self,graph, starting_vertex):
              
        self.distances = {vertex[1]: inf for vertex in graph}
        self.distances[starting_vertex[1]] = 0
        self.visited=set()
        self.heapped = [(starting_vertex)]
        self.path_tracker=[]
        self.solution_length=0
        while self.heapped:
            self.solution_length+=1
            self.heurstic,self.current_vertex = heapq.heappop(self.heapped)    
            self.visited.add(self.current_vertex)
            self.path_tracker.append(self.current_vertex)
            while self.heapped:
                top=heapq.heappop(self.heapped)
                self.visited.add(top[1])
                

            for neighbor, weight,heurstic in graph[(self.heurstic-self.distances[self.current_vertex],self.current_vertex)]:
                if neighbor in self.visited:continue
                if heurstic==0:
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

time_taken=[]
solution_length=[]
graph=instance_of_graph.graph
instance_for_AStar=AStartAlgoritm()
all_nodes=list(graph.keys())

for start_node in all_nodes:
    #We can convert a second into mili second by multiplying with 1000
    start_time=(time.time())*1000
    length=0
    for target_node in all_nodes:
        #If the start node is the target node, we don't need to compute a shortest distance.
        if start_node==target_node:continue        
        start=start_node
        target=target_node 
        instance_for_Heurisitic_graph_builder.targe_initializer(target=target)
        instance_for_Heurisitic_graph_builder.heuristicGraphBuilder()
        distance=instance_for_Heurisitic_graph_builder.distance_from_node_to_target_node(start_node)

        graph=instance_for_Heurisitic_graph_builder.ready_heurstic_graph
        instance_for_AStar.shortest_path(graph,(int(distance),start)) 
        length+=instance_for_AStar.solution_length
        
        #path_tracker, given below, is the list of the shortest path according to the A* algorithm
        print("\nStart node: {}\n End node:{} ".format(start,target))
        print("\tShortest Path\t=>",instance_for_AStar.path_tracker)
    #We can convert a second into mili second by multiplying with 1000   
    end_time=(time.time())*1000
    time_taken.append(end_time-start_time)
    solution_length.append(length/len(graph))
print("\nThe Average time taken to find a solution of A* algorithm  : {} milli seconds"\
    .format(np.sum(time_taken)/len(time_taken)))
print("The Average solution length to find a solution with A* Alogrithm: {} "\
    .format(np.sum(solution_length)/len(solution_length)))

