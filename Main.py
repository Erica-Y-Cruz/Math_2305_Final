
from algorithms import prims
from Functions.graph_operations import graph_cost

text = input("Please provide a graph to run the TSP on ")

text = input("PLease provide a starting vertex ")
T = prims(G, v)
print('Optimal Tree is {T}')

print('')

print(f'Optimal cost: {graph_cost(T)}')