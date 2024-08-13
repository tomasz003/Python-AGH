import numpy as np
import matplotlib.pyplot as plt

def line(a,b):
    #arrays, as in MatLab
    x=np.linspace(a,b,100)
    y=np.sin(x)

    #plotting
    plt.plot(x,y)


