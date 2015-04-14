 temp = [s.index(node1), s.index(node2)]
    temp.sort()
    index1, index2 = temp 
    if index1 == 0 and index2 == len(s) - 1: snew[index1 :] = snew[index2 : : -1]
    elif index1 == 0: snew[index1 : index2 + 1] = snew[index2 : : -1]
    elif index2 == len(s) - 1: snew[index1 : ] = snew[index2 : index1 - 1 : -1]
    else: snew[index1 : index2 + 1] = snew[index2 : index1 - 1 : -1]



    def settemp(points, T):
    i = 0
    change = []
    s = range(len(points))
    while T > 0.001:
        c = totallen(points, s)
        node1, node2 = ran.sample(s, 2)   
        snew = list(s)
        snew[node1], snew[node2] = snew[node2], snew[node1] 
        cnew = totallen(points, snew)
        delta = cnew - c
        change.append(delta)
        if delta <= 0:
            s = snew
        else:
            r = ran.uniform(0, 1)
            if r <= math.exp(- (1.0 * delta / T  )): s = snew
        i = i + 1
        T = 0.99 * T
    return  sum(change) / len(change) 