#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    values = []
    weights = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        values.append(int(parts[0]))
        weights.append(int(parts[1]))

    items = len(values)
    a = opt(items,capacity,values,weights)
    
    value = 0
    weight = 0
    taken = []

    value = a[0]
    taken = [1 if i in a[1] else 0 for i in range(items)]
    
    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data

def estimate(items, capacity, arg):
    est = 0
    for i in range(items):
        if capacity > 0:
            temp = arg[i]
            if capacity >= temp[1]:
                est = est + temp[0]
                capacity = capacity - temp[1]
            else:
                est = est + float(capacity) * temp[0] / temp[1]
                capacity = 0
        else: 
            break
    return est
    
# data 
def node(n,val, cap, est,taken,flag):
    return {'number': n,'value': val, 'capacity': cap, 'estimate': est,'taken' : taken,'flag': flag}
          
# node :{ 'number':n, 'value': natural, 'capacity': natural, 'estimate': natural,'flag':flag}
"""
def eli_taken(a,b):
    return [a[j] for j in range(len(a)) if j not in b]
   """ 
def opt(items,capacity,values,weights):
    arg = zip(values,weights)
    arg = zip(arg,range(items))
    arg.sort(key = lambda x : float(x[0][0]) / x[0][1], reverse = True)
    a,b = zip(*arg)
    arg = list(a)
    a1,b1 = zip(*arg)
    temp = b1
    values = a1
   
    stack = []
    est = estimate(items,capacity,arg)
    stack.append(node(-1,0,capacity,est,[],'root'))
    best_val = 0
    
    while stack != []:
        root = stack.pop()
        root_nth = root['number']
        root_val =  root['value']
        root_cap =  root['capacity']
        root_taken =  root['taken']
        i = root_nth + 1       
        length = items - i -1

        if  root_val > best_val:
            best_val = root_val
            node1 = root
        if i < items:
            right_val = root_val
            right_cap =  root_cap
            right_est = estimate(length, right_cap,arg[i+1:]) + right_val
            if right_est > best_val:
                stack.append(node(i,right_val,right_cap,right_est,root_taken,'r'))
            left_cap = root_cap - temp[i]
            if left_cap >= 0:
                left_val = root_val + values[i]
                left_est = estimate(length, left_cap, arg[i+1:]) + left_val
                if left_est > best_val:
                    stack.append(node(i,left_val,left_cap,left_est, root_taken + [i],'l'))
    temp2 = node1['taken']
    temp3 = [b[i] for i in temp2]
    return [best_val,temp3]


import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        input_data_file = open(file_location, 'r')
        input_data = ''.join(input_data_file.readlines())
        input_data_file.close()
        print solve_it(input_data)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)'

