import networkx as nx
import numpy as np
from scipy.spatial import distance
from collections import defaultdict

def graph_analyzer(num_Cu, Cu_data, Cu_bond, num_elem, h_start, h_end):
    
    G = nx.DiGraph()
    #G_0 = nx.Graph()
    nodes = []
    index = -1

    for m in range(num_Cu):
        if (h_start<float(Cu_data[m][3])<h_end):
            index = index + 1
            G.add_node('Cu'+str(index))
            #G_0.add_node('Cu'+str(index))
            nodes.append(m)
            
    coordinates = defaultdict(list)
    dist = np.empty((index+1, index+1))
    
    for i in range(index+1):
        for j in range(1,4):
            coordinates[i].append(float(Cu_data[nodes[i]][j]))
    for i in range(index+1):
        for j in range(index+1):
            dist[i][j] = distance.euclidean(coordinates[i], coordinates[j])

    for a in range(index):
        for b in range (index):
            if ((dist[a][b]<Cu_bond) & (a!=b)):
                G.add_edge('Cu'+str(a),'Cu'+str(b))
                #G_0.add_edge('Cu'+str(a),'Cu'+str(b))
                    
    counter = 0
    cycles = list(nx.simple_cycles(G))
        
    for c in range(len(cycles)):
        if (len(cycles[c]) == num_elem):
            counter = counter + 1

    #largest_cc = max(nx.connected_components(G_0), key=len)
            
    G.clear()
    #G_0.clear()
    
    return int(counter/2), 0, 0