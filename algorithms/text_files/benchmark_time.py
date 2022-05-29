import matplotlib.pyplot as plt 
import numpy as np

# You can draw a graph by commenting eigher of the  two
# meaning average_solution_time and average_solution_length.
algorithms = ("BFS","DFS","DIJKSTRA","A*")
y = np.arange(len(algorithms))
average_solution_time_for_bfs=1.26705322265625
average_solution_time_for_dfs=1.0845458984375
average_solution_time_for_dijkstra=10.639999999999997
average_solution_time_for_A_star=10.59591064453125
performance = [average_solution_time_for_bfs,
               average_solution_time_for_dfs,
               average_solution_time_for_dijkstra,
               average_solution_time_for_A_star]

plt.bar(y, performance, align='center', alpha=0.5)
plt.xticks(y, algorithms)
plt.ylabel('Average time')
plt.xlabel("Algorithms")
plt.title('Average solution time')
plt.show()

# algorithms = ("BFS","DFS","DIJKSTRA","A*")
# y = np.arange(len(algorithms))
# average_solution_length_for_bfs=11.25
# average_solution_length_for_dfs=10.880
# average_solution_length_for_dijkstra=10.640
# average_solution_length_for_A_star=3.755
# performance = [average_solution_length_for_bfs,
#                average_solution_length_for_dfs,
#                average_solution_length_for_dijkstra,
#                average_solution_length_for_A_star]

# plt.bar(y, performance, align='center', alpha=0.5)
# plt.xticks(y, algorithms)
# plt.ylabel('Average solution length')
# plt.xlabel("Algorithms")
# plt.title('Average solution length of those four algorithms')

# plt.show()


