import TrussSolver as ts
import numpy as np

# These are gonna be the x and y coordinates of each joint
nodes = np.array([
    [0,0],      #0
    [4,0],      #1
    [0,4],      #2
    [4,4],      #3
    [0,8],      #4
    [4,8],      #5
    [4,12],     #6
    [8,12],     #7
    [8,8],      #8
    [12,8]      #9
], dtype=object)

# This is gonna model the relationship between joint indicies
connections = np.array([
    [1,2,3],        #0
    [0,3],          #1
    [0,3,4],        #2
    [0,1,2,4,5],    #3
    [2,3,5,6],      #4
    [3,4,6,7,8],    #5
    [4,5,7],        #6
    [6,5,8,9],      #7
    [5,7,9],        #8
    [7,8]           #9
],dtype=object)

# Actually creating the truss
truss1 = ts.Truss(nodes, connections)

# Adding test loads
truss1.addLoad(0,[-60,-280])
truss1.addLoad(1,[0,360])
truss1.addLoad(9,[60,-80])

# Solving the truss
truss1.solve()

# Printing out an image of the truss
trussdraw = ts.PgTruss(truss1,800)
trussdraw.drawNodes()

"""
Blue is compression
Red is tension
Y'all might have to download the dependancies which are numpy and pygame
"""