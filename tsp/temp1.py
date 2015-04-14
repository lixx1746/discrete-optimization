def SA(points,  T_i, T_f, timelimit, n = 1):
    T_i = settemp(points, 10000000000)
    print T_i
    
    sbest = range(len(points))
    best = totallen(points, sbest)
    
    for i in range(n):
        print 'this is the ', i , 'th'
        s, c = sbest, best
        sum_t = 0
        T = T_i
        while T > T_f:
            t, sbest1, s = timer(trial, points, s, T)
            best1 = totallen(points, sbest1)
            if best > best1:
                best = best1
                sbest = sbest1
            sum_t = sum_t + t 
            T = T_i * math.pow(1.0 * T_f / T_i, sum_t / timelimit)
            #print T
        #if i == 0: T_i = sum(change)/ len(change)
        #print T_i
        print best