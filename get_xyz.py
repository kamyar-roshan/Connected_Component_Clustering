import numpy as np

def get_xyz(RDF_data, num_Cu):
    
    coordinates = np.empty((num_Cu, 3))
    
    for i in range(num_Cu):
        for j in range(1,4):
            coordinates[i, j-1] = (float(RDF_data[i][j]))
            
    x = coordinates[:, 0]
    y = coordinates[:, 1]
    z = coordinates[:, 2]
            
    return x, y, z