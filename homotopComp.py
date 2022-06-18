
#from syslog import setlogmask
import numpy as np


from sympy.solvers import solve
from sympy import Symbol

x = Symbol('x')
y = Symbol('y')
def intersect (dr,seg):

    exp=x *(seg[1]-seg[0])+seg[0]-(dr[0]+y*dr[1])
    
    sol=solve(exp, [x,y])
    
    if len(sol)==0:
        return [False,sol]
    else:
        if 0<=sol[x]<=1 and 0<=sol[y]:
            return [True,sol]
        else: 
            return[False,sol]
        
        
def findTranslation(seg,SegTranslation_DataFrame):
    for i in range(len(SegTranslation_DataFrame)):
        iEqual=isEqual(seg,SegTranslation_DataFrame.iloc[i,0])
        if(iEqual):
            return [True,SegTranslation_DataFrame.iloc[i,1]]
    return [False]
def isEqual(seg1,seg2):
    if np.linalg.norm(seg1[0]-seg2[0])==0 and np.linalg.norm(seg1[1]-seg2[1])==0:
        return True
    else:
        return False
    
def closestIntersection(dr,DtF):
    output={'SegmentIndex':-1, 'ycoefficient':-1}
    for i in range(len(DtF.index)):
        res=intersect(dr,DtF.iloc[i,0])
        if res[0]==True:
            if res[1][y]>0 and (output['SegmentIndex']==-1 or (output['ycoefficient']>=0 and output['ycoefficient']>res[1][y])):
                output['SegmentIndex']=i
                output['ycoefficient']=res[1][y]
    return output