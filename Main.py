'''
Created on Nov 13, 2014

@author: Bumsub
'''

import matplotlib.pyplot as plt
import numpy as np
import pysal
from pysal.core.util.shapefile import shp_file
import Polygon as poly


if __name__ == '__main__':
    
    
    '''
    # Convex hull
    points = np.random.rand(30, 2)
    hull = ConvexHull(points)
    convexHullArray=[]
    for j in hull.vertices:
        convexHullArray.append([points[j,0], points[j,1]])
    print convexHullArray
    print convexHullArray[1]    
    '''
    
    points = np.random.rand(30,2)
    convexhull = poly.makeConvexHull(points)
    print convexhull
    
    '''
    print(type(points))
    plt.plot(points[:,0], points[:,1], 'o')
    for simplex in hull.simplices:
        plt.plot(points[simplex,0], points[simplex,1], 'k-')
    plt.plot(points[hull.vertices,0], points[hull.vertices,1], 'r--', lw=2)
    plt.plot(points[hull.vertices[0],0], points
             [hull.vertices[0],1], 'ro')
    plt.show()
    '''
    # Read shapefile
    shp = pysal.pysal.core.FileIO.FileIO.open('testdata/cities.shp','r')  # @UndefinedVariable
    shp.seek(0)
    '''
    poly = shp.read(1)
    ring = poly[0]
    for i in ring:
        print i
    '''
    
    for i in shp:
        print i

