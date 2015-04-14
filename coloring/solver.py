#!/usr/bin/python
# -*- coding: utf-8 -*-

import random as ran
import time
import math

neighbours = {}

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    global neighbours
    lines = input_data.split('\n')
    first_line = lines[0].split()
    node_count = int(first_line[0])
    edge_count = int(first_line[1])
    nodes = range(node_count)
    neighbours = dict((s, []) for s in nodes)
    edges = []
    for i in range(1, edge_count + 1):
        line = lines[i]
        parts = line.split()
        edges.append((int(parts[0]), int(parts[1])))
    for e in edges:
        w, v = e
        neighbours[w].append(v)
        neighbours[v].append(w)

    
   
    #bestdict, best = mysolver1(nodes, 3500, 100)
    #nodes, it_max, timelimit, kmax
    bestdict, best = SA2(nodes, 3000, 1000, 1000)
    # prepare the solution in the specified output format
    #bestdict, best = mysolver1(nodes, 50000, 1000)
    output_data = str(best) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, bestdict.values()))

    return output_data

def greedy(nodes):
    s = nodes[0]
    color = dict((s, -1) for s in nodes)
    color[s] = 0
    for node in nodes[1 : ]:
        rank = [color[s] for s in neighbours[node] if color[s] != -1]
        rank.sort()
        rank = set(rank)
        ans = 0
        for i in rank:
            if ans < i:
                break
            ans = ans + 1
        color[node] = ans

    return color, max(color.values()) + 1

def mysolver(nodes, kmax, timelimit):
    start = time.time()
    end = start
    color, num = greedy(nodes)
    best = num
    bestdict = color
    k = 0
    while k < kmax and (end - start) < timelimit:
        per = range(num)
        ran.shuffle(per)
        nodes = [s for i in per for s in nodes if color[s] == i]
        color, num = greedy(nodes)
        if num < best:
            best = num
            bestdict = color
        k = k + 1
        num = best
        end = time.time()   

    return bestdict, best

def mysolver1(nodes, kmax, timelimit):
    start = time.time()
    end = start
    color, num = greedy(nodes)
    best = num
    bestdict = color
    k = 0
    while k < kmax and (end - start) < timelimit:
        per = range(num)
        ran.shuffle(per)
        #nodes = [s for i in per for s in nodes if color[s] == i]
        newnodes = []
        for i in per:
            partial = []
            for s in nodes:
                if color[s] == i:
                    partial.append(s)
            ran.shuffle(partial)
            newnodes = newnodes + partial
        nodes = newnodes
        color, num = greedy(nodes)
        if num < best:
            best = num
            bestdict = color
        num = best
        k = k + 1
        end = time.time()   

    return bestdict, best

def mysolver2(nodes, kmax, timelimit, restart):
    bestdict, best = mysolver1(nodes, kmax, timelimit)
    i = 0
    while i < restart:
        ran.shuffle(nodes)
        color, num= mysolver1(nodes, kmax, timelimit)
        if num < best:
            best = num
            bestdict = color 
        i = i + 1
    return bestdict, best

def WelshPowell(nodes):
    nodes.sort(key = lambda x : len(neighbours[x]), reverse = True)
    c = 0
    color = {}
    while nodes:
        
        s = nodes[0]
        colored = []
        neig = []
        color[s] = c;
        neig = neig + neighbours[s]
        colored.append(s);
        for node in nodes:
            if node not in neig:
                color[node] = c
                neig = neig + neighbours[node]
                colored.append(node)
        nodes = [s for s in nodes if s not in colored]      
        c = c + 1
    return color, c


def SA(nodes, itmax, timelimit, kmax):
    start = time.time()
    end = start
    bestdict, best = WelshPowell(nodes)
    bestcolor = set(range(best))
    it = 0
    while it < itmax and (end - start) < timelimit:
        k = 0
        colordict, count = bestdict, best
        color = bestcolor
        while k < kmax:
            node = ran.choice(nodes)    
            using_existed = ran.uniform(0.3, 1)
            using_new = math.exp(-2 *  k) #need prune
            if using_existed > using_new:
                ncolor = set(colordict[s] for s in neighbours[node])
                pool = [c for c in color if c not in ncolor] + [colordict[node]]
                newcolor = ran.choice(pool)
            else:
                #samecolor = [n for n in nodes if colordict[n] is colordict[node]]
                newcolor = max(color) + 1
                #for n in samecolor: colordict[n] = newcolor
            colordict[node] = newcolor
            k = k + 1
            color = set(colordict.values())

        if len(color) < best:
            best = len(color)
            bestdict = colordict 
            bestcolor = color

        end = time.time()
        it = it + 1
    return bestdict, best

def SA2(nodes, itmax, timelimit, kmax):
    start = time.time()
    end = start
    bestdict, best = WelshPowell(nodes)
    bestcolor = set(range(best))
    it = 0
    while it < itmax and (end - start) < timelimit:
        k = 0
        colordict, count = bestdict, best
        color = bestcolor
        while k < kmax:
            node = ran.choice(nodes)    
            ncolor = set(colordict[s] for s in neighbours[node])
            pool = [c for c in color if c not in ncolor]
            if pool:
                newcolor = ran.choice(pool)
                colordict[node] = newcolor
            k = k + 1
            
        color = set(colordict.values())
        if len(color) < best:
            best = len(color)
            bestdict = colordict 
            bestcolor = color

        end = time.time()
        it = it + 1
    return bestdict, best




import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        input_data_file = open(file_location, 'r')
        input_data = ''.join(input_data_file.readlines())
        input_data_file.close()
        with open('output_data', 'w') as myFile:
            myFile.write(solve_it(input_data))
        print solve_it(input_data)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/gc_4_1)'

