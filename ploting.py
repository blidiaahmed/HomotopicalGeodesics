from homotopComp import *
import pandas as pd
import unittest
from test import *
import ipdb
import numpy as np
import matplotlib.pyplot as plt
drt=[np.array([0.35,0.25]),np.array([0.5,0.2])]

for i in range(100):
    #print(drt)
    res=closestIntersection(drt,DtF)
    Intersectionpoint=(drt[0]+res["ycoefficient"]*drt[1])
    #print(Intersectionpoint,res["ycoefficient"])
    plt.plot([drt[0][0],Intersectionpoint[0]],[drt[0][1],Intersectionpoint[1]])
    drt[0]=Intersectionpoint+DtF.iloc[res["SegmentIndex"],1]
    
    
drt
plt.savefig('plot.pdf')  