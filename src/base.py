## Author DrFargo
## Created: 2021-02-07

import matplotlib
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt

class starshipSimulation:
    def Render(self, filename):
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax = self.XYZLabels(ax, 24000) 
        plt.savefig(filename + ".png")
        plt.show()
        
    def XYZLabels(self, ax, Limit):
        TopAlt = np.max(Limit)
        Lim = TopAlt*1.1
        ax.set_zlim3d([0,2*Lim])
        ax.set_xlim3d([-Lim,Lim])
        ax.set_ylim3d([-Lim,Lim])
        ax.set_xlabel("Eastings")
        ax.set_ylabel("Northings")
        ax.set_zlabel("Altitude")

class AxisData:
    LabelDict = {
        "Time":"Time (s)",
        "AngleOfAttack":"Angle of Attack (rad)",
        "Thrust":"Thrust (N)",
        "X":"Eastings",
        "Y":"Northings",
        "Z":"Altitude",
    }