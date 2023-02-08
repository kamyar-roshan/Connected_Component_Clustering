import numpy as np
from scipy.spatial import distance
from collections import defaultdict

def dist_array(num_Cu, Cu_data):
    
    coordinates = defaultdict(list)
    dist = np.empty((num_Cu, num_Cu))
    for i in range(num_Cu):
        for j in range(1,4):
            coordinates[i].append(float(Cu_data[i][j]))
    for i in range(num_Cu):
        for j in range(num_Cu):
            dist[i][j] = distance.euclidean(coordinates[i], coordinates[j])
            
    return dist