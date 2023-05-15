#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 16:14:31 2023

@author: clement
"""

from random import shuffle

##<--------------------------------------------
##Personal functions defined
##--------------------------------------------->
def adjacentNodes(node,grid):
    '''Returns list of all adjacent nodes of node in grid
    node : first argument, a tuple 
    grid : second argument, a grid made of lists
    '''
    adj = []
    i,j = node[0],node[1]
    m,n = len(grid), len(grid[0])
    
    if grid[i][j] !='x':
        if i+1<m and grid[i+1][j] !='x':
            adj.append((i+1,j))
        if j+1<n and grid[i][j+1] !='x':
            adj.append((i,j+1))
        if i-1>=0 and grid[i-1][j] !='x':
            adj.append((i-1,j))
        if j-1>=0 and grid[i][j-1] !='x':
            adj.append((i,j-1))
    return adj

def possibleNodes(grid):
    '''Returns the number of nodes robot can visite in grid
    Its argument is a grid made of lists
    '''
    num_nodes = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]!='x':
                num_nodes += 1
            
    return num_nodes
            
def strToGrid(string):
    '''Returns a grid based on the argument
    Argument is a string separete by \n charactar 
    '''
    grid = []
    i = 0
    num_col = 0
    num_line = 0
    #Remove all spaces in string
    string = string.replace(' ','')
    #Get column numbers
    while string[i]!='\n':
        i = i+1
    
    num_col = i
    #Get line numbers
    num_line = int(len(string)/num_col)
    
    #Remove the \n
    string = string.replace('\n','')
    
    #Complete the grid by using string
    line = []
    for i in range(num_line):
        for j in range(num_col):
            line.append(string[i*num_col+j])
        #Add a line to grid
        grid.append(line)
        #
        line = []
    return grid

def dfs(node,grid, color, sons):
    '''Returns a dictionary of 
    
    '''
    color[node] = 'grey'
    #Get all adjacent nodes of node
    neighbor =  adjacentNodes(node,grid)
    #Reorganize elements of neighbor to make movement random from node
    shuffle(neighbor)
    #For each element of neighbor, create relation father/son between nodes
    for adj in neighbor:
        if color[adj] == 'white' :
            sons[node] = adj
            dfs(adj,grid, color, sons)
    color[node] = 'black'

def makeAPath(sons,m,n):
    '''Returns a paths from A to B or None if there is no
    sons : dictionary
    m, n : grid dimensions
    '''
    v = (0,0)
    paths = []
    while v!=None:
        paths.append(v)
        if v != (m-1,n-1):
            v = sons[v]
        else:
            v = None
    if paths[-1] == (m-1,n-1):
        return paths
    return None


##<------------------------------------------------

##------------------------------------------------>
        
def count_paths(input_string):
    '''Returns the number of elements of variable set_of_all_paths
    This variable contains all possible ways to move from A to B
    input_string 
    '''
    # parse the string input here, possibly calling other functions that you’ve
      # written in your Python code file
    
    # possibly call other functions that you’ve written in your Python code
    # file to count the number of paths
    #convert input_string in to grid
    grid = strToGrid(input_string)
    #get dimension of grid
    m, n = len(grid), len(grid[0])
    #list of all paths from A to B
    set_of_all_paths = []
    #Node A
    node = (0,0)
    #color dictionnary : color[(0,0)] is one of gray, white and black 
    # color[(0,0)] = white means node (0,0) is not visited
    # color[(0,0)] = gray means is in process visited
    # color[(0,0)] = black means is visited
    color = {}
    #sons dicionnary : sons[(0,0)] = (1,0) means that following node of (0,0) is (1,0)
    sons = {}
    
    #Use dfs algorithm 3^(m+n) times to taking account of all paths from A to B
    #When robot move, it can visite 3 node maximum
    #m+n represents the depth maximum in in grid
    for k in range(3**(m+n)):
        #Initialization of variables color, sons
        for i in range(m):
            for j in range(n):
                color[(i,j)] = 'white'
                sons[(i,j)] = None
            
        #Compute dfs to get list of sons which contains node into robot move
        #from a given node
        dfs(node,grid, color, sons)
        #Compute a paths with sons variable
        paths = makeAPath(sons,m,n)
        #Add path if it is a paths that taking account all nodes robot can visite
        if paths not in set_of_all_paths and paths and len(paths) == possibleNodes(grid) :
            set_of_all_paths.append(paths)

    # return the (integer) number of paths
    return len(set_of_all_paths)

##<--------------------------------------------
##Test
##--------------------------------------------->
string1 = 'A . . . .\n. . . . . \n. . . . B'
string2 = 'A . . . .\n. . . x B'
string3 = 'A . .\nx x B'
string4 = 'A . . .\n. . . .\n. . . .\n. . x B'
string5 = 'A . . .\n. . . B'
string6 = 'A . .\n. . B'
string7 = 'A . . .\nx . . B'
string8 = 'A . . . . . .\n. . . . . . x\n. . x . x . .\n. . . . . . .\n. . . . . . B'
string9 = 'A . . . . . . x x\nx . . . . . . . .\nx . . . . . . . B'
string10 = 'A . .\n. . .\n. . B'
string11 = 'A . . . . .\n. . . . . .\n. . . . . .\n. . . . x B'



print(string1)
print('number of paths = ',count_paths(string1))
print(string2)
print('number of paths = ',count_paths(string2))
print(string3)
print('number of paths = ',count_paths(string3))
print(string4)
print('number of paths = ',count_paths(string4))
print(string5)
print('number of paths = ',count_paths(string5))
print(string6)
print('number of paths = ',count_paths(string6))
print(string7)
print('number of paths = ',count_paths(string7))
#print(string8)
#print('number of paths = ',count_paths(string8))
#print(string9)
#print('number of paths = ',count_paths(string9))
print(string11)
print('number of paths = ',count_paths(string11))









