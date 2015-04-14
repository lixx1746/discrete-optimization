def totallen(points, solution):
    obj = length(points[solution[-1]], points[solution[0]])
    for index in range(0, nodeCount-1):
        obj += length(points[solution[index]], points[solution[index+1]])


def SA(points, T, factor, freezelimit, timelimit, trialmax):
    s = range(0, len(points))
    c = totallen(points, s)
    best, sbest = c, s
    start = time.time()
    end = start
    freezecount = 0
    while freezecount < freezelimit and (end - start) < timelimit:
        trial = 0
        chageflag = False
        while trial < trialmax:
            flag = False
            node1, node2 = ran.sample(s[1 :], 2)   
            snew = list(s)
            snew[node1], snew[node2] = snew[node2], snew[node1] 
            cnew = totallen(points, snew)
            delta = cnew - c
            if delta <= 0: flag = True
            else:
                r = ran.uniform(0, 1)
                if r <= math.exp(- (1.0 * delta / T)): flag = True
            if flag:
                s = snew
                c = cnew
            if best > cnew:
                best = cnew
                sbest = snew
                chageflag = True
            trial = trial + 1
        T = factor * T
        if chageflag: freezecount = 0
        else: freezecount = freezecount + 1
        end = time.time()
    return sbest, best