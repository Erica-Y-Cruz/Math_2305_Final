from Functions.reading_writing_functions import get_graph
from Functions.graph_operations import incident_edges, cost, graph_cost, min_cost_incident_edge
from Algorithms.prims_algorithm import prims

G = get_graph('G1.txt')
    
print(f'V(G) = {G[0]}')
print('')
print(f'E(G) = {G[1]}')
print('')

# initialize tree 
T = ([3, 1], [(3, 1),(1, 4)] )

print(f' T = {T}')
print('')

print("Edges:")
for e in G[1]:
    print(e)


print("Incident Edges:", incident_edges(G, T))


for e in incident_edges(G, T):
    print(f'Edge {e} with cost {cost(G, e)}')
    

#print(f'The cost of edge (1,3) is {cost(G, (1,3))}')
print("Minimum cost incident edge:", min_cost_incident_edge(G,T))
print(f'Total weight: {graph_cost(G)}')


