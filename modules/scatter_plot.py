import matplotlib.pyplot as plt
import numpy as np

def scatter_RDF(x, y):
    
    plt.scatter(x, y)
    plt.title('RDF')
    plt.xlabel('radius (A)')
    plt.ylabel('4. g(r)')
    plt.show()
