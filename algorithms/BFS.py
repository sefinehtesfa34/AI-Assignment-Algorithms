import queue
import numpy as np 
from build_graph import instance_of_graph
import time
start_time=time.time()  
graph=instance_of_graph.graph

def bfsFunction(start,target):
    initial_node=start
    queu=queue.deque([initial_node])
    visited=set(initial_node)
    path_tracker={start:None}
    global length
    length=0
    while queu:
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
    return path_tracker
all_nodes=list(graph.keys())
solution_length=[]
time_taken=[]
length=0
for start_node in all_nodes:
    #We can convert a second into mili second by multiplying with 1000
    start_time=(time.time())*1000
    solution_len=0
    for target_node in all_nodes:
        #If the start node is the target node, we don't need to compute a shortest distance.
        if start_node==target_node:continue        
        start=start_node
        target=target_node
        path_tracker=bfsFunction(start,target)
        solution_len+=length
        print(start,target)
        temp=target
        shortest_path=[]          
        while path_tracker[temp]:
            shortest_path.append(temp)
            temp=path_tracker[temp]
        shortest_path.append(start)
        shortest_path=shortest_path[::-1]
        print(shortest_path)

    #We can change a second into milli second by multiplying with 1000
    end_time=(time.time())*1000
    solution_length.append(solution_len/len(graph))    
    time_taken.append(end_time - start_time)
    
average_solution_length=np.sum(solution_length)/len(solution_length)
average_time_taken=np.sum(time_taken)/len(time_taken)
print("The average solution length for BFS alogrithm: {} ".format(average_solution_length))
print("The average time taken for BFS algorithm: {}".format(average_time_taken))

