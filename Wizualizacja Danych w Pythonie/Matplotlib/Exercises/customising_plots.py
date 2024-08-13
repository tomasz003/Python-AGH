import numpy as np
import matplotlib.pyplot as plt

def line(a,b):
    #arrays, as in MatLab
    x=np.linspace(a,b,100)
    y=np.sin(x)

    #plotting & customizing
    plt.plot(x,y, linestyle="--", color="red", label="Sine Curve")
    plt.title("Sine Curve")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()

