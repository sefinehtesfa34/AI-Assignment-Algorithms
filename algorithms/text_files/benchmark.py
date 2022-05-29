# import matplotlib.pyplot as plt
# fig=plt.figure()
# ax=fig.add_axes([0,0,1,1])
# algorithms = ["BFS","DFS","DIJKSTRA","A*"]
# average_solution_length=[11.225,10.879,10.640,3.755]
# average_times=[1.26705322265625,1.0845458984375,10.639999999999997 , 10.59591064453125]
# ax.bar(algorithms,average_solution_length)
# plt.show()
# import matplotlib.pyplot as plt
# fig = plt.figure()
# ax = fig.add_axes([0,0,1,1])
# langs = ['C', 'C++', 'Java', 'Python', 'PHP']
# students = [23,17,35,29,12]
# plt.xlabel("Algorithms")
# plt.ylabel("Solution length")
# ax.bar(langs,students)

# ax.set_xticks(students, ('G1', 'G2', 'G3', 'G4', 'G5'))
# plt.show()
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects = ("BFS","DFS","DIJKSTRA","A*")
y_pos = np.arange(len(objects))
performance = [11.225,10.879,10.640,3.755]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Solution length')
plt.xlabel("Algorithms")
plt.title('Solution Length')

plt.show()