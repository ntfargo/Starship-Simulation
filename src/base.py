## Author DrFargo
## Created: 2021-02-07

import matplotlib
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt

class starshipSimulation:  
    def Starship():
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        plt.show()
    
    def saveSimulation(filename):
        plt.savefig(filename + ".png")
        
class AxisData:
    LabelDict = {
        "Time_0":"Time (s)",
        "AngleOfAttack_0":"Angle of Attack (rad)",
        "Thrust_0":"Thrust (N)",
    }