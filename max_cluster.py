from modules.search import search
from modules.merge import merge

def max_cluster(dist, Cu_bond, num_Cu, num_clusters):
    
    count = 0
    clusters = {}
    for i in range(num_Cu):
        for j in range(num_Cu):
            if ((dist[i][j]<Cu_bond) & (i!=j)):
                if ((search(clusters, i) == None) & (search(clusters, j) == None)):
                    clusters[str(count)] = []
                    clusters[str(count)].append([i])
                    clusters[str(count)].append([j])
                    count+=1
                elif (search(clusters, i) == None):
                    clusters[str(search(clusters, j))].append([i])
                elif (search(clusters, j) == None):
                    clusters[str(search(clusters, i))].append([j])
                elif ((search(clusters, i) != None) & (search(clusters, j) != None)):
                    if (search(clusters, i) != search(clusters, j)):
                        merge(clusters, i, j)
    for i in range(num_Cu):
        if (search(clusters, i) == None):
            clusters[str(count)] = []
            clusters[str(count)].append([i])
            count+=1
        
    num_clusters.append(len(clusters))
    max_size = 1
    
    for i in clusters:
        if (len(clusters[str(i)]) > max_size):
            max_size = len(clusters[str(i)])
    return max_size