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

average_times=[]
average_solutions=[]
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
    average_times.append(average_time_taken)
    average_solutions.append(average_solution_length)

x_axis=np.array([0,20,30,40,50,60,70,80])
y_axis=average_solutions


plt.plot(x_axis,y_axis)
plt.xlabel("Number of nodes")
plt.ylabel("Solution Length")
plt.legend("solutionLength",loc="lower right")
plt.show()


