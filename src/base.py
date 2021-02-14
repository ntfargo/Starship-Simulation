## Author DrFargo
## Created: 2021-02-07
## Latest update: 2021-02-12

import matplotlib
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt

class starshipSimulation:
    def parameters(self, g, lox, engines):
        gravity = g
        tlox = lox
        rapteng = engines*2.3
        m_fuel = 1.8
        m_ox = 2.2
        
    #def DragForce(self, v):
        

    def Render(self, filename):
        fig = plt.figure()
        ax = fig.gca(projection='3d') 
        ax = self.XYZLabels(ax, 12000) 
        plt.savefig(filename + ".png")
        plt.show()
        
    def explode(self,t):
        ax.text(0, 0, 0, "red", color='red')
        return y[1]
        
    def XYZLabels(self, ax, Limit):
        TopAlt = np.max(Limit)
        Lim = TopAlt*1.1
        ax.set_zlim3d([0,2*Lim])
        ax.set_xlim3d([-Lim,Lim])
        ax.set_ylim3d([-Lim,Lim])
        ax.set_xlabel("Eastings")
        ax.set_ylabel("Northings")
        ax.set_zlabel("Altitude")