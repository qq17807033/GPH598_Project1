
from scipy.spatial.qhull import ConvexHull
 

def __init__(self, params):
    '''
    Constructor
    '''
        
def makeConvexHull(points, incremental=False, qhull_options=None):
    hull = ConvexHull(points, incremental=False, qhull_options=None)
    convexHullArray=[]
    for j in hull.vertices:
        convexHullArray.append([points[j,0], points[j,1]])
    return convexHullArray