# -*- coding: utf-8 -*-

# shows edges not in tree
def incident_edges(G, T):
    edges = []
    for e in G[1]:
        for vertex_a in T[0]:
            for vertex_b in T[0]:
                #considers edges already seen
                if (vertex_a in e) and (e not in T[1]) and (e not in edges):
                            edges.append(e)
    return edges


# returns cost of edges 
def cost(G, e):
 return G[1][e]

def initialize_tree(v):
    return (([v], []))



 # find the minimum edge of a list
 # return minimum edge
    
def min_cost_incident_edge(G, T):
    edges = incident_edges(G, T)
    min_e = edges[0]
    
    for e in edges:
        if cost(G, e) < cost(G, min_e):
            min_e = e
      
    return min_e

# graph_cost returns the total weight of a graph
# sum of edges

def graph_cost(G):
    weight = 0
    for c in G[1]:
        weight += cost(G, c)
        
    return weight
    
    
# add each edge until there are no more edges
        
 