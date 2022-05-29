from collections import defaultdict
from math import radians, cos, sin, asin, sqrt
from build_graph import instance_of_graph
class HeuristicFunction:
    def distance_finder(self,latitude_one, longitude_one, latitude_two, longitude_two):
        self.latitude_one, \
        self.longitude_one, \
        self.latitude_two, \
        self.longitude_two \
        = map(radians, [latitude_one, longitude_one, latitude_two, longitude_two])
        
        self.longitude_difference = self.longitude_two - self.longitude_one 
        self.latitude_difference = self.latitude_two - self.latitude_one 
        self.distance = sin(self.latitude_difference/2)**2 \
            + cos(self.latitude_one) \
            * cos(self.latitude_two) \
            * sin(self.longitude_difference/2)**2
        self.distance= 2 * asin(sqrt(self.distance)) 
        self.distance_in_km = 6371* self.distance
        
        return self.distance_in_km
instance_of_heuristic_function=HeuristicFunction()
#The distance_finder_function above computes the distance between the target city and each of the other
#cities by using the given latitude and longitude.
  
class HeuristicGraphBuilder:
    def targe_initializer(self,target):
        self.target=target

    def distance_from_node_to_target_node(self,node):
        return self.heurstic_function[node]
            
    def heuristicGraphBuilder(self):
        self.graph=instance_of_graph.graph
        self.cities_latitude_and_longitude={}
        with open("algorithms/text_files/latitude_and_longitude.txt") \
            as latitude_and_longitude:
            
            self.text_files=latitude_and_longitude.readlines()
            for line in self.text_files:
                line_to_list=line.strip().split()
                self.cities_latitude_and_longitude[line_to_list[0]]=\
                    [float(line_to_list[1]),float(line_to_list[2])]
        #Target, the destination city that we need to compute the heuristic functions 
        # for each of other cities
        target=self.target
        self.heurstic_function={}
        target_latitude,target_longitude=self.cities_latitude_and_longitude[target]
        for city in self.graph:
            city_latitude,city_longitude=self.cities_latitude_and_longitude[city]
            distance=instance_of_heuristic_function.distance_finder(\
                                latitude_one=target_latitude,\
                                latitude_two=city_latitude,\
                                longitude_one=target_longitude,\
                                longitude_two=city_longitude)
            self.heurstic_function[city]=distance
            
        self.ready_heurstic_graph=defaultdict(list)
        for city in self.heurstic_function:
            for neighor in self.graph[city]:
                #Making aready heuristic graph with keys of graph 
                # is tupled of heuristic values and 
                # city(node) i.e (heurisitic_vallues,city) and values of 
                #Each key has a list of (neighor1,weight,heuristic value of neighor1) for 
                # #all neighors of each node.
                # see below line of code, it builds this heuristic graph I described above. 
                self.ready_heurstic_graph[int(self.heurstic_function[city]),\
                    city].append((neighor[0],int(neighor[1]),int(self.heurstic_function[neighor[0]])))
#heuristicGraphBuilder as the name suggests, it builds a graph by considering the edge distance 
#and the heuristic functions for each city on the given text file, see all the files. 
#This class will be exported to the A_star_algorithm file.