from Functions.reading_writing_functions import get_graph
from Functions.graph_operations import incident_edges, cost, graph_cost

G = get_graph('G1.txt')
    
print(f'V(G) = {G[0]}')
print('')
print(f'E(G) = {G[1]}')
print('')

# initialize tree 
T = ([3, 1], [(3, 1),(1, 4)] )

print(f' T = {T}')
print('')
for e in G[1]:
    print(e)

#print(incident_edges(G, T))


# print(f'The cost of edge (1,3) is {cost(G, (1,3))}')
    
for e in incident_edges(G, T):
    print(f'Edge {e} with cost {cost(G, e)}')
    
print(graph_cost)

