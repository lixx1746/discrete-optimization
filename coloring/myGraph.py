class myGraph(dict):
    def __init__(self,vs = [], es = []):
        """creat a new graph, vs is a list of vertices, 
        es is a list of edges."""
        for v in vs:
            self.add_vertex(v)
        for e in es:
            self.add_edge(e)

    def add_vertex(self,v):
        """ add v to the graph"""
        self[v] = []
    
    def add_edge(self,e):
        """ add e to the graph by adding an entry in both directions,
        if there is already an edge connecting these vertices, the new
        edge replaces it"""
        v,w = e
        if w not in self[v] or v not in self[w]: 
            self[v].append(w)
            self[w].append(v)

class Edge(tuple):
    def __new__(cls, e1, e2):
        return tuple.__new__(cls, (e1,e2))
    
    def __repr__(self):
        return 'Edge(%s, %s)' % (repr(self[0]), repr(self[1]))

    __str__ = __repr__


class Vertex(object):
    def __init__(self, label =''):
        self.label = label

    def __repr__(self):
        return 'Vertex(%s)' %repr(self.label)

    __str__ = __repr__
