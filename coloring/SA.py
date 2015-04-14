import random as ran
import time
import math
import WelshPowell as we
import GreedyBasic as gr
neighbours = {0 : [1,7], 1 : [0, 3], 2 : [3], 3 : [1, 2, 8, 10], 4 : [5, 10], 5 :[4, 6], 6 : [5, 7 , 10], 7 : [0, 8, 9, 10, 6],
 8 : [3, 7 , 9], 9 : [7, 8 , 10], 10 : [3, 6, 4, 9, 7]}

def SA(nodes, itmax, timelimit, kmax):
	start = time.time()
	end = start
	colordict, count = we.WelshPowell(nodes)
	color = set(range(count))
	bestdict, best = colordict, count
	it = 0
	while it < itmax and (end - start) < timelimit:
		k = 0
		while k < kmax:
			node = ran.choice(nodes)	
			using_existed = ran.uniform(0, 1)
			#using_new = math.exp(-k) #need prune
			using_new = math.exp((-2.0 *  k) / kmax)
			samecolor = [n for n in nodes if colordict[n] is colordict[node]]
			if using_existed > using_new:
				pool = [c for c in color for s in neighbours[node] if c is not colordict[s]]
				newcolor = ran.choice(pool + [colordict[node]])
				colordict[node] = newcolor
			else:
				newcolor = max(color) + 1
				for n in samecolor: colordict[n] = newcolor
			k = k + 1
			color = set(colordict.values())
		if len(color) < best:
			best = len(color)
			bestdict = colordict 
		end = time.time()
		it = it + 1
	return bestdict, best


if __name__ == '__main__':
	#print neighbours
	d, c = SA(range(11), 10, 5, 5)
	print d
	print 'the number is', c

