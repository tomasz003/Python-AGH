import numpy as np
import matplotlib.pyplot as plt

def histogram(seed):
    np.random.seed(seed)

    # generating random numbers
    ran_1 = np.random.randn(1000)
    plt.hist(ran_1, bins=30)
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.title("Histogram")