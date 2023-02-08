import os
import time
import networkx as nx
import matplotlib.pyplot as plt
from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

main_path = "/Users/kamyar/Box Sync/van Duin Group/Projects/Silicon Copper Interaction/CCC_algorithm/"
os.chdir(main_path)
t_start = time.time()

from modules.RDF import RDF
from modules.plot import plot
from modules.saveit import saveit
from modules.get_xyz import get_xyz
from modules.get_frame import get_frame
from modules.dist_array import dist_array
from modules.max_cluster import max_cluster
from modules.scatter_plot import scatter_RDF

file_name = '500_80'
file = open('raw_data(xmolout)/'+file_name, "r")
data_lines = file.readlines()
num_atoms = int(float(data_lines[0]))
num_frames = int((len(data_lines))/(num_atoms+2))
num_Si = 512
num_Cu = num_atoms - num_Si
Cu_bond = 3
time_step = 0.25
max_cluster_time = []
num_clusters = []
sim_time = []

G=nx.Graph()
G.add_nodes_from(["a","b","c","d","e"])
G.add_edges_from([("a","b"),("b","c"), ("c","a"), ("b","d"), ("d","e"), ("e","a")])
list(nx.simple_cycles(G))

if __name__ == '__main__':

    for l in range(num_frames):
        Cu_data = get_frame(l, num_Si, num_atoms, data_lines)
        dist = dist_array(num_Cu, Cu_data)
        max_cluster_time.append(max_cluster(dist, Cu_bond, num_Cu, num_clusters))
        sim_time.append(l*time_step)

saveit(max_cluster_time, num_clusters, sim_time, file_name)
plot(max_cluster_time, 'Size of the biggest Cu cluster')
plot(num_clusters, 'Number of Cu clusters')
index = max_cluster_time.index(max(max_cluster_time))
RDF_data = get_frame(index, num_Si, num_atoms, data_lines)
x, y, z = get_xyz(RDF_data, num_Cu)
(r, g) = RDF(x, y, z, S=100, rMax=15, dr=0.02)
scatter_RDF(r, g)
print('Total time: ' + str(round(((time.time() - t_start)/(60)), 2)) + ' minutes')