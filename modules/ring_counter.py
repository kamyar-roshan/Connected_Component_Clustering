import networkx as nx

def ring_counter(num_Cu, dist, Cu_bond, num_elem):
    
    G = nx.DiGraph()

    for m in range(num_Cu):
        G.add_node('Cu'+str(m+1))

    for a in range(num_Cu):
            for b in range (num_Cu):
                if ((dist[a][b]<Cu_bond) & (a!=b)):
                    G.add_edge('Cu'+str(a),'Cu'+str(b))
                    
    counter = 0
    cycles = list(nx.simple_cycles(G))
        
    for c in range(len(cycles)):
        if (len(cycles[c]) == num_elem):
            counter = counter + 1
            
    G.remove_edges_from(list(G.edges))
    return int(counter/2)
