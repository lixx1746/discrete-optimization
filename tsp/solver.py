#!/usr/bin/python
# -*- coding: utf-8 -*-

import math
import random as ran
import time
from collections import namedtuple
import matplotlib.pyplot as plt

Point = namedtuple("Point", ['x', 'y'])
table = []

def length(point1, point2):
    return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    nodeCount = int(lines[0])

    points = []
    for i in range(1, nodeCount+1):
        line = lines[i]
        parts = line.split()
        points.append(Point(float(parts[0]), float(parts[1])))

    # build a trivial solution
    # visit the nodes in the order they appear in the file
    creat_table(points)
    #print table
    solution, obj = SA(points, math.pow(10, 10), 0.001, 30, 5)

    # calculate the length of the tour
    #obj = length(points[solution[-1]], points[solution[0]])
    #for index in range(0, nodeCount-1):
    #    obj += length(points[solution[index]], points[solution[index+1]])

    # prepare the solution in the specified output format
    output_data = str(obj) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, solution))

    return output_data

def creat_table(points):
    len1 = len(points)
    #len1 = 5
    global table
    for i in range(len1 - 1):   #0, 1, 2, 3
        part = []
        for j in range(i + 1, len1):
            part.append(length(points[i], points[j]))
        table.append(part)

def totallen(solution):
    #print table
    nodeCount = len(solution)
    temp = [solution[-1], solution[0]];
    temp.sort()
    a, b = temp
    #print a, b
    obj = table[a][b - a - 1]
    for index in range(0, nodeCount-1):
        temp1 = [solution[index], solution[index + 1]];
        temp1.sort()
        a1, b1 = temp1
        obj += table[a1][b1 - a1 - 1]
    return obj

change = []

def trial(points, s, T):
    global change
    c = totallen(s)
    sbest, best = s, c
    node1, node2 = ran.sample(s, 2)
    #temp = [node1, node2]
    #temp.sort()
    #index1, index2 = temp 
    #if(index1 == 0): index1 = index1 + 1
    #if(index2 == len(s) - 1): index2 = index2 - 1   
    snew = list(s)
    temp = [s.index(node1), s.index(node2)]
    temp.sort()
    index1, index2 = temp 
    if index1 == 0 and index2 == len(s) - 1: snew[index1 :] = snew[index2 : : -1]
    elif index1 == 0: snew[index1 : index2 + 1] = snew[index2 : : -1]
    elif index2 == len(s) - 1: snew[index1 : ] = snew[index2 : index1 - 1 : -1]
    else: snew[index1 : index2 + 1] = snew[index2 : index1 - 1 : -1]
    
    #node11, node12 = ran.sample(snew, 2)
    #snew1 = list(snew)
    #temp1 = [snew.index(node11), snew.index(node12)]
    #temp1.sort()
    #index11, index12 = temp 
    #if index11 == 0 and index12 == len(s) - 1: snew1[index11 :] = snew1[index12 : : -1]
    #elif index11 == 0: snew1[index11 : index12 + 1] = snew1[index12 : : -1]
    #elif index12 == len(s) - 1: snew1[index11 : ] = snew1[index12 : index11 - 1 : -1]
    #else: snew1[index11 : index12 + 1] = snew1[index12 : index11 - 1 : -1]

   
    #snew[index1 : index2 + 1] = reversed(snew[index1 : index2 + 1])
    cnew = totallen(snew)
    change.append(cnew)
    delta = cnew - c
    if delta <= 0:
        s = snew
        if best > cnew:
            sbest = snew 
    else:
        r = ran.uniform(0, 1)
        if r <= math.exp(- (1.0 * delta / T )): s = snew

           
    return sbest, s

def greedy(points):
    first = 0
    sol = range(len(points))
    #print sol
    s = []
    while True:
        sol.remove(first)
        #print sol
        s.append(first)
        if len(s) == len(points): return s
        next = min(sol, key = lambda x : length(points[first], points[x]))
        first = next



def timer(f, *arg):
    start = time.time()
    sbest, s = f(*arg)
    end = time.time()
    return end - start, sbest, s

      
def SA(points,  T_i, T_f, timelimit, n = 1):
    #T_i = settemp(points, 10000000000)
    #print T_i
    
    sbest = range(len(points))
    #sbest = greedy(points)
    best = totallen(sbest)
    print sbest
    
    for i in range(n):
        print 'this is the ', i , 'th'
        s, c = sbest, best
        sum_t = 0
        T = T_i
        while T > T_f:
            t, sbest1, s = timer(trial, points, s, T)
            best1 = totallen(sbest1)
            if best > best1:
                best = best1
                sbest = sbest1
            sum_t = sum_t + t 
            #print sum_t
            T = T_i * math.pow(1.0 * T_f / T_i, sum_t / timelimit)
        print best


    
    
    return sbest, best


import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        input_data_file = open(file_location, 'r')
        input_data = ''.join(input_data_file.readlines())
        input_data_file.close()
        print solve_it(input_data)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/tsp_51_1)'

