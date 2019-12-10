# -*- coding: utf-8 -*-

from Functions.graph_operations import min_cost_incident_edge, incident_edges
from Functions.reading_writing_functions import get_graph

#prims algorithm adds edges with the smallest weight, 
#never forms a circuit and stops when n-1 edges have been added

#start at smallest edge
#then compare the edge to its adjacent edges, 
#if edge is smaller take that path, double check to see 
#if that edge is not in the list then mark as visited
#then add to the list, then so on and so on until there are no more edges. 
    

e = 0
    
def initialize_tree(v):
    return (([v], []))

def prims(G, v):
    G = get_graph(G[0])
    T = initialize_tree(v)
    path = min_cost_incident_edge(G, T)
    available = incident_edges(G, T)
  
    # if length of tree's vertices is not the same length of graph's vertices
    while (len(T[0])) != (len(G[0])):
        #e = min_cost_incident_edge(G, T)
        #add e and its vertices to T
        
        
        for path in available:
            for vertex_a in T[0]:
                for vertex_b in T[0]:
                    if vertex_b not in G and G.graph[vertex_a][vertex_b] !=0:
                        T[1].append((path))
                    
            for edge in T[1]:
                for ver in edge:
                    if ver not in T[0]:
                        T[0].append(ver)
                        available = incident_edges(G, T)
                        path = min_cost_incident_edge(G, T)
    return T

