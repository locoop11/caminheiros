


class Node(object):
    def __init__(self, name):
        """
        Requires: name is a string
        """
        self.name = name
    def getName(self):
        return self.name
    def __str__(self):
        return self.name



class Edge(object):
    def __init__(self, src, dest, cost):
        """
        Requires: src and dst Nodes
        """
        self.src = src
        self.dest = dest
        self.cost = cost
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def getCost(self):
        return self.cost
    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName() + '(' + str(self.cost) + ')'

class Digraph(object):
    # nodes is a list of the nodes in the graph
    # edges is a dict mapping each node to a list of its children
    def __init__(self):
        self.nodes = []
        self.edges = {}
    def addNode(self, node):
        if node in self.nodes:
            raise ValueError('Duplicate node')
        else:
            self.nodes.append(node)
            self.edges[node] = []
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        cost = edge.getCost()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append([dest, cost])
    def childrenOf(self, node):
        if node in self.edges:
            return list(self.edges[node].items())
        else:
            return []
    def hasNode(self, node):
        return node in self.nodes

class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)

        

def printPath(path):
    """
    Requires: path a list of nodes
    """
    result = ''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + '->'
    return result



def DFS(graph, start, end, path, shortest, pathCost, shortestCost):
    path = path + [start]
    print('Current DFS path:', printPath(path))
    if start == end:
        return path
    for node, cost in graph.childrenOf(start):
        if node not in path: #avoid cycles
            if shortest == None or pathCost + cost < shortestCost:
                newPath = DFS(graph, node, end, path, shortest, pathCost + cost, shortestCost)
                if newPath != None:
                    shortest = newPath
                    shortestCost = pathCost + cost
    return shortest

def search(graph, start, end):
    return DFS(graph, start, end, [], None, 0, float('inf'))

 

def search(graph, start, end):
    """
    Requires:
    graph  a Digraph;
    start and end are nodes
    Ensures:
    shortest path from start to end in graph
    """
    return DFS(graph, start, end, [], None)



def testSP():
    """
    this functions retuns the shortest path in from of
    """
    nodes = []
    for name in range(6): #Create 6 nodes
        nodes.append(Node(str(name)))
    g = Digraph()
    for n in nodes:
        g.addNode(n)
    g.addEdge(Edge(nodes[0],nodes[1]))
    g.addEdge(Edge(nodes[1],nodes[2]))
    g.addEdge(Edge(nodes[2],nodes[3]))
    g.addEdge(Edge(nodes[2],nodes[4]))
    g.addEdge(Edge(nodes[3],nodes[4]))
    g.addEdge(Edge(nodes[3],nodes[5]))
    g.addEdge(Edge(nodes[0],nodes[2]))
    g.addEdge(Edge(nodes[1],nodes[0]))
    g.addEdge(Edge(nodes[3],nodes[1]))
    g.addEdge(Edge(nodes[4],nodes[0]))
    sp = search(g, nodes[0], nodes[5])
    print('Shortest path found by DFS:', printPath(sp))


testSP()

    
    
