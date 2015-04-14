neighbours = {0 : [1,7], 1 : [0, 3], 2 : [3], 3 : [1, 2, 8, 10], 4 : [5, 10], 5 :[4, 6], 6 : [5, 7 , 10], 7 : [0, 8, 9, 10, 6],
 8 : [3, 7 , 9], 9 : [7, 8 , 10], 10 : [3, 6, 4, 9, 7]}

import random as ran
import time
def greedy(nodes):
	s = nodes[0]
	color = dict((s, -1) for s in nodes)
	color[s] = 0
	for node in nodes[1 : ]:
		rank = [color[s] for s in neighbours[node] if color[s] is not -1]
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
		end = time.time()
		k = k + 1	
	return bestdict, best 
import sys

if __name__ == '__main__':
	#print neighbours
	d, c = mysolver(range(11), 10, 5)
	print d
	print 'the number is', c