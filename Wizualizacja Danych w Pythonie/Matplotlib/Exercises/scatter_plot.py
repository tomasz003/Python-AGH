import numpy as np
import matplotlib.pyplot as plt

def scatter(seed):
    np.random.seed(seed)

    # generating random numbers
    ran_1 = np.random.rand(100)
    ran_2 = np.random.rand(100)
    colors = np.random.rand(100)
    print(ran_1)
    print(ran_2)
    print(colors)

    plt.scatter(ran_1, ran_2, c=colors)
