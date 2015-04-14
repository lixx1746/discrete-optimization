#neighbours are given;
neighbours = {0 : [1,7], 1 : [0, 3], 2 : [3], 3 : [1, 2, 8, 10], 4 : [5, 10], 5 :[4, 6], 6 : [5, 7 , 10], 7 : [0, 8, 9, 10, 6],
 8 : [3, 7 , 9], 9 : [7, 8 , 10], 10 : [3, 6, 4, 9, 7]}

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

import sys

if __name__ == '__main__':
	#print neighbours
	d, c = WelshPowell(range(11))
	print d
	print 'the number is', c


