import queue
import time 
import numpy as np 
from collections import defaultdict
import matplotlib.pyplot as plt
from A_star_algorithm import AStartAlgoritm

from dijkstara_shortest_path import Dijkistra 
class MatplolibGraph(Dijkistra,AStartAlgoritm):
    def __init__(self,file_name) -> None:
        self.fileName=file_name
        self.graph=defaultdict(list)
        
    def graphBuilder(self,connection):
        self.graph[connection[0]].append((connection[1],connection[2]))
        self.graph[connection[1]].append((connection[0],connection[2]))
     
    def file_reader(self):
        with open(self.fileName,'r') as file:
            connections=file.readlines()
            for connection in connections:
                self.graphBuilder(connection.strip().split(' '))
    
matplolib_graph1=MatplolibGraph("algorithms/text_files/connections.txt")
matplolib_graph2=MatplolibGraph("algorithms/text_files/connections2x.txt")
matplotlib_graph3=MatplolibGraph("algorithms/text_files/connections3x.txt")
matplotlib_graph4=MatplolibGraph("algorithms/text_files/connections4x.txt")
matplolib_graph5=MatplolibGraph("algorithms/text_files/connections5x.txt")
matplolib_graph6=MatplolibGraph("algorithms/text_files/connections6x.txt")
matplotlib_graph7=MatplolibGraph("algorithms/text_files/connections7x.txt")
matplotlib_graph8=MatplolibGraph("algorithms/text_files/connections8x.txt")

list_of_instances=[matplolib_graph1,
                   matplolib_graph2,
                   matplotlib_graph3,
                   matplotlib_graph4,
                   matplolib_graph5,
                   matplolib_graph6,
                   matplotlib_graph7,
                   matplotlib_graph8]

average_times_for_dijkstra=[]
average_solutions_for_dijkstra=[]
for instance in list_of_instances:
    

    instance.file_reader()

    graph=instance.graph


    for key in graph:
        graph[key]=dict(graph[key])
        
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
            instance.shortest_path(graph,start,target)
            length+=instance.solution_length
            # print("Outside the graph: ",instance.solution_length)
            # print(start,target)
            # print(instance.output)
        #We can change a second into milli second by multiplying with 1000
        end_time=(time.time())*1000
        solution_length.append(length/len(graph))    
        time_taken.append(end_time - start_time)
    average_solution_length=np.sum(solution_length)/len(solution_length)
    average_time_taken=np.sum(time_taken)/len(time_taken)
    average_times_for_dijkstra.append(average_time_taken)
    average_solutions_for_dijkstra.append(average_solution_length)

print(average_solutions_for_dijkstra)
print(average_times_for_dijkstra)






matplolib_graph1=MatplolibGraph("algorithms/text_files/connections.txt")
matplolib_graph2=MatplolibGraph("algorithms/text_files/connections2x.txt")
matplotlib_graph3=MatplolibGraph("algorithms/text_files/connections3x.txt")
matplotlib_graph4=MatplolibGraph("algorithms/text_files/connections4x.txt")
matplolib_graph5=MatplolibGraph("algorithms/text_files/connections5x.txt")
matplolib_graph6=MatplolibGraph("algorithms/text_files/connections6x.txt")
matplotlib_graph7=MatplolibGraph("algorithms/text_files/connections7x.txt")
matplotlib_graph8=MatplolibGraph("algorithms/text_files/connections8x.txt")

list_of_instances=[matplolib_graph1,
                   matplolib_graph2,
                   matplotlib_graph3,
                   matplotlib_graph4,
                   matplolib_graph5,
                   matplolib_graph6,
                   matplotlib_graph7,
                   matplotlib_graph8]



def dfsFunction(start,target):
    initial_node=start
    stack =[initial_node]
    visited=set(initial_node)
    path_tracker={start:None}
    length=0
    while stack :
        length+=1
        frontier=stack .pop()
        if frontier==target:
                break
        for child in graph[frontier]:
            temp=child[0]
            if temp not in visited:
                visited.add(temp)
                stack.append(temp)
                if temp not in path_tracker:
                    path_tracker[temp]=frontier
    return length


total_length=0
average_times_for_dfs=[]
average_solutions_for_dfs=[]
for instance in list_of_instances:   
    instance.file_reader()
    graph=instance.graph
    for key in graph:
        graph[key]=dict(graph[key])
        
    all_nodes=list(graph.keys())
    solution_length=[]
    time_taken=[]
    for start_node in all_nodes:
        #We can convert a second into mili second by multiplying with
        start_time=(time.time())
        length=0
        for target_node in all_nodes:
            #If the start node is the target node, we don't need to compute a shortest distance.
            if start_node==target_node:continue        
            start=start_node
            target=target_node
            solution_len = dfsFunction(start,target)
            length+=solution_len
            
            #We can change a second into milli second by multiplying with
        end_time=(time.time())
        solution_length.append(length/len(graph))    
        time_taken.append(end_time - start_time)
    average_solution_length_for_dfs=np.sum(solution_length)/len(solution_length)
    average_time_taken_for_dfs=np.sum(time_taken)/len(time_taken)
    average_times_for_dfs.append(average_time_taken_for_dfs)
    average_solutions_for_dfs.append(average_solution_length_for_dfs)
    
average_solution_length=np.sum(solution_length)/len(solution_length)
average_time_taken=np.sum(time_taken)/len(time_taken)

print(average_solutions_for_dfs)
# print(average_times_for_dfs)

matplolib_graph1=MatplolibGraph("algorithms/text_files/connections.txt")
matplolib_graph2=MatplolibGraph("algorithms/text_files/connections2x.txt")
matplotlib_graph3=MatplolibGraph("algorithms/text_files/connections3x.txt")
matplotlib_graph4=MatplolibGraph("algorithms/text_files/connections4x.txt")
matplolib_graph5=MatplolibGraph("algorithms/text_files/connections5x.txt")
matplolib_graph6=MatplolibGraph("algorithms/text_files/connections6x.txt")
matplotlib_graph7=MatplolibGraph("algorithms/text_files/connections7x.txt")
matplotlib_graph8=MatplolibGraph("algorithms/text_files/connections8x.txt")

list_of_instances=[matplolib_graph1,
                   matplolib_graph2,
                   matplotlib_graph3,
                   matplotlib_graph4,
                   matplolib_graph5,
                   matplolib_graph6,
                   matplotlib_graph7,
                   matplotlib_graph8]



def bfsFunction(start,target):
    initial_node=start
    queu =queue.deque([initial_node])
    visited=set(initial_node)
    path_tracker={start:None}
    length=0
    while queu :
        length+=1
        frontier=queu.popleft()
        if frontier==target:
                break
        for child in graph[frontier]:
            temp=child[0]
            if temp not in visited:
                visited.add(temp)
                queu.append(temp)
                if temp not in path_tracker:
                    path_tracker[temp]=frontier
    return length


total_length=0
average_times_for_bfs=[]
average_solutions_for_bfs=[]
for instance in list_of_instances:   
    instance.file_reader()
    graph=instance.graph
    for key in graph:
        graph[key]=dict(graph[key])
        
    all_nodes=list(graph.keys())
    solution_length=[]
    time_taken=[]
    for start_node in all_nodes:
        #We can convert a second into mili second by multiplying with
        start_time=(time.time())
        length=0
        for target_node in all_nodes:
            #If the start node is the target node, we don't need to compute a shortest distance.
            if start_node==target_node:continue        
            start=start_node
            target=target_node
            solution_len = bfsFunction(start,target)
            length+=solution_len
            
            #We can change a second into milli second by multiplying with
        end_time=(time.time())
        solution_length.append(length/len(graph))    
        time_taken.append(end_time - start_time)
    average_solution_length_for_dfs=np.sum(solution_length)/len(solution_length)
    average_time_taken_for_dfs=np.sum(time_taken)/len(time_taken)
    average_times_for_bfs.append(average_time_taken_for_dfs)
    average_solutions_for_bfs.append(average_solution_length_for_dfs)
    
average_solution_length=np.sum(solution_length)/len(solution_length)
average_time_taken=np.sum(time_taken)/len(time_taken)

print(average_solutions_for_bfs)
# print(average_times_for_bfs)






# x_axis=np.array([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8])
# y_axis=average_solutions_for_dfs
# plt.plot(x_axis,y_axis)

x1=np.array([1,2,3,4,5,6,7,8])
y1= average_solutions_for_bfs
x2=np.array([1,2,3,4,5,6,7,8])
y2=average_solutions_for_dfs
x3=np.array([1,2,3,4,5,6,7,8])
y3=average_solutions_for_dijkstra

# plt.plot(x_axis,y_axis)

# plt.ylim(0,100)
plt.plot(x1, y1, label = "BFS")
plt.plot(x2, y2, label = "DFS")
plt.plot(x3, y3, label = "DIJKSTRA")
plt.legend()
plt.show()


# x_axis=np.array([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8])
# y_axis=average_solutions_for_dijkstra
# plt.plot(x_axis,y_axis)

# # x_axis=np.array([1,2,3,4,5,6,7,8])
# # y_axis=average_solutions_for_dfs
# # plt.plot(x_axis,y_axis)

# # plt.xlabel("Number of nodes")
# # plt.ylabel("Solution Length")
# plt.legend("solutionLength",loc="lower right")
# plt.show()


