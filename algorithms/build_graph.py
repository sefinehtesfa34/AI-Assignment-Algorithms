from collections import defaultdict 
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def graphBuilder(self,connection):
        self.graph[connection[0]].append((connection[1],connection[2]))
        self.graph[connection[1]].append((connection[0],connection[2]))
        
        
instance_of_graph=Graph()

with open('algorithms/text_files/connections.txt','r') as text_file:
    connections=text_file.readlines()
    for connection in connections:
        instance_of_graph.graphBuilder(connection.strip().split(' '))
         
# for connection in instance_of_graph.graph:
    # print(connection,"=>",instance_of_graph.graph[connection])
    
    
