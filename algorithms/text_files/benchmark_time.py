import matplotlib.pyplot as plt 
import numpy as np
objects = ("BFS","DFS","DIJKSTRA","A*")
y_pos = np.arange(len(objects))
performance = [1.26705322265625,1.0845458984375,10.639999999999997 , 10.59591064453125]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Average time')
plt.xlabel("Algorithms")
plt.title('Average solution time')

plt.show()