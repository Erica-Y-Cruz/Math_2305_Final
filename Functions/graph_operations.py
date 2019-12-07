# -*- coding: utf-8 -*-

def incident_edges(G, T):
    edges = []
    for e in G[1]:
        for v in T[0]:
            #doesn't consider edges already seen
            if v in e and e not in T[1]:
                
                # if v in e and e not in T[0] ??
                edges.append(e)
        #remove edges that make cycles
        
    return edges

def cost(G, e):
    return G[1][e]


# add a min_cost_incident_edge(G, T)
    # find the minimum of a list
    # return minimum edge
    
def min_cost_incident_edge(G, T):
    edges = incident_edges
    min_e = edges[0]
    
    for i in range(1, len(edges)):
        
        return min_e
    
# graph_cost returns the total weight of a graph
# sum of edges
        
def graph_cost(G, e):
    weight = [] 
    for n in range(len(G[2])):
        weight.add(G[2])
        n -=1
        
    return weight
    
    
    # add each edge until there are no more edges
    # for i in range(len(G[2])):
        
        
    
    
    
    
    
def initialize_tree(v):
    return (([v], []))