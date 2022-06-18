from homotopComp import *

import pandas as pd
import unittest




seg1=np.array([np.array([1,0]),np.array([1,1])])
seg2=np.array([np.array([1,0]),np.array([1,1])])
DtF=pd.DataFrame(
    [[np.array([np.array([0,0]),np.array([1,0])])
      ,np.array([0,2])],
     [np.array([np.array([1,0]),np.array([2,0])])
      ,np.array([0,1])],
     [np.array([np.array([2,0]),np.array([2,1])])
      ,np.array([-2,0])],
     [np.array([np.array([2,1]),np.array([1,1])])
      ,np.array([0,-1])],
     [np.array([np.array([1,1]),np.array([1,2])])
      ,np.array([-1,0])],
     [np.array([np.array([1,2]),np.array([0,2])])
      ,np.array([0,-2])],
     [np.array([np.array([0,2]),np.array([0,1])])
      ,np.array([1,0])],
     [np.array([np.array([0,1]),np.array([0,0])])
      ,np.array([2,0])]
     ])
seg3=np.array([np.array([0,0]),np.array([1,0])])
seg4=np.array([np.array([0,3]),np.array([1,0])])
class testHomotopy(unittest.TestCase):
    def test_SegmentEquality(self):
        self.assertTrue(isEqual(seg1,seg2))
        
    def test_findSegmentInDataFrame(self):
        res =findTranslation(seg3,DtF)
        self.assertEqual(len(res),2)
        iFound=res[0]
        self.assertTrue(iFound)
        resTranslation=res[1]
        self.assertEqual(resTranslation[0],0)
        self.assertEqual(resTranslation[1],2)
        
        res =findTranslation(seg4,DtF)
        self.assertEqual(len(res),1)
        iFound=res[0]
        self.assertTrue(not iFound)
class intersections(unittest.TestCase):
    def test_intersect(self):
        dr=[np.array([0,0.25]),np.array([0.5,0])]
        seg=[np.array([1,0]),np.array([1,1])]
        res=intersect(dr,seg)
        self.assertTrue(res[0])
        self.assertTrue(res[1][x]==0.25)
        self.assertTrue(res[1][y]==2.0)
    def test_closestIntersection(self):
        dr=[np.array([0,0.25]),np.array([0.5,0])]
        res=closestIntersection(dr,DtF)
        self.assertEqual(res['SegmentIndex'],2)
        self.assertEqual(res['ycoefficient'],4)
        
        
        
            
        
        
        
if __name__=='__main__':
    unittest.main()