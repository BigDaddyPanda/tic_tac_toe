from math import sqrt
from random import randint
from itertools import permutations
# make dict as {(x,y):point}

def init_map(size):
    pos={(e//size,e%size):e for e in range(size**2 )}
    return pos

#to smoothen the work
def get(grid,xy,i,j):
    if(xy!=(-1,-1)): return grid.get((xy[0]+i,xy[1]+j),-1)
    return -1

#to smoothen things even more than previous smoothing
def getxy(grid,x):
    for i in grid.items():
        if i[1]==x:
            return i[0]
    return (-1,-1)

#BEHOOOLD THE GLORY OF A NEW SUN
def collinear_3x3(p0, p1, p2):
    x1, y1 = p1[0] - p0[0], p1[1] - p0[1]
    x2, y2 = p2[0] - p0[0], p2[1] - p0[1]
    return abs(x1 * y2 - x2 * y1) < 1e-12

#BEHOOOLD THE GLORY OF A NEW SUN
def collinear_4x4(p0, p1, p2, p3):
    x1, y1 = p1[0] - p0[0], p1[1] - p0[1]
    x2, y2 = p2[0] - p0[0], p2[1] - p0[1]
    x3, y3 = p3[0] - p0[0], p3[1] - p0[1]
    return (abs(x1 * y2 - x2 * y1) < 1e-12)and(abs(x1 * y3 - x3 * y1) < 1e-12)

#BEHOOOLD THE GLORY OF A NEW SUN
def collinear_5x5(p0, p1, p2, p3,p4):
    x1, y1 = p1[0] - p0[0], p1[1] - p0[1]
    x2, y2 = p2[0] - p0[0], p2[1] - p0[1]
    x3, y3 = p3[0] - p0[0], p3[1] - p0[1]
    x4, y4 = p4[0] - p0[0], p4[1] - p0[1]
    return (abs(x1 * y2 - x2 * y1) < 1e-12)and(abs(x1 * y3 - x3 * y1) < 1e-12)and(abs(x1 * y4 - x4 * y1) < 1e-12)

#return neighbors of a point
def neighbor(x,grid):
    xy=getxy(grid,x)
    r=[-1,0,1]    
    return [get(grid,xy,i,j) for i in r for j in r if get(grid,xy,i,j)!=-1 and get(grid,xy,i,j)!=x]
# #print(neighbor(3,init_map(3)))
#let's get'm bois

def winning_condition_3(grid):
    s= [sorted([grid[a],grid[b],grid[c]]) 
    for a in grid.keys() 
    for b in grid.keys() 
    for c in grid.keys() 
    if a!=b and b!=c and c!=a 
    and collinear_3x3(a,b,c)
    and grid[b] in neighbor(grid[a],grid)
    and grid[c] in neighbor(grid[b],grid)
        ]
    v=[]
    for x in s: 
        if x not in v: v.append(x)
    return v
def winning_condition_4(grid):
    s= [sorted([grid[a],grid[b],grid[c],grid[d]]) 
        for a in grid.keys() 
        for b in grid.keys() 
        for c in grid.keys() 
        for d in grid.keys() 
        if a!=b and a!=c and a!=d and b!=c and b!=d and c!=d
        and collinear_4x4(a,b,c,d)
        and grid[b] in neighbor(grid[a],grid)
        and grid[c] in neighbor(grid[b],grid)
        and grid[d] in neighbor(grid[c],grid)
        ]
    v=[]
    for x in s: 
        if x not in v: v.append(x)
    return v

# print(winning_condition_3(init_map(3)))