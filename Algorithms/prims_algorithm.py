# -*- coding: utf-8 -*-

def prims(G1):
    G = get_graph(G1)
    T = initialize_tree(G, v)
    
    while T[0] != G[0]:
        e = min_cost_edge(G, T)
        #add e and its vertices to T
        
    return T

#prims algorithm adds edges with the smallest weight, 
#never forms a circuit and stops when n-1 edges have been added

#start at smallest edge
#then compare the edge to its adjacent edges, 
#if edge is smaller take that path, double check to see 
#if that edge is not in the list then mark as visited
#then add to the list, then so on and so on until there are no more edges. 
    


    
