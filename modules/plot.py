import matplotlib.pyplot as plt

def plot(data, label):
    plt.plot(data)
    plt.ylabel(label)
    plt.xlabel('frame')
    plt.show()
