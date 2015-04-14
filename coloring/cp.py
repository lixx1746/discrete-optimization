def mysolver(k):
    #print neigbours, nodes
    values = dict((s,''.join(map(str, range(k)))) for s in nodes)
    return search(values)



def search(values):
    if values is False: 
        return False
    if all(len(values[s]) == 1 for s in nodes): return values;
    n,s = min((len(values[s]), s) for s in nodes if len(values[s]) > 1)
    return some(search(assign(values.copy(), s, d)) 
        for d in values[s])

def assign(values, node, d):
    other_values = values[node].replace(d, '')
    #print other_values
    if all(eliminate(values, node, d2) for d2 in other_values):
        return values
    else:
        return False


def eliminate(values, node, d):
    if d not in values[node]:
        return values
    values[node] = values[node].replace(d, '')

    if len(values[node]) == 0:
        return False
    elif len(values[node]) == 1:
        d2 = values[node]
        if not all(eliminate(values, s2, d2) for s2 in neigbours[node]):
            return False

    
        dplaces = [s for s in neigbours[node] if d in values[s]]
        if len(dplaces) == 0:
            return False
        elif len(dplaces) == 1:
            if not assign(values, dplaces[0], d):
                return False

    return values

def some(seq):
    "Return some element of seq that is true."
    for e in seq:
        if e: return e
    return False