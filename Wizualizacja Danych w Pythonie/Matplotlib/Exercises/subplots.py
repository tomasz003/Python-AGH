import numpy as np
import matplotlib.pyplot as plt

def subplots(a,b):
    x=np.linspace(a,b,100)
    sin_x=np.sin(x)
    cos_x=np.cos(x)

    #subplots:
    fig, axs = plt.subplots(2, 1, figsize=(6, 6))

    #sin:
    axs[0].plot(x, sin_x)
    axs[0].set_title("Sine Curve")

    #cos:
    axs[1].plot(x, cos_x)
    axs[1].set_title("Cosine Curve")

    plt.tight_layout()
