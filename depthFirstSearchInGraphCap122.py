


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
        
        existingEdges = self.edges[src]
        for (n, cost) in existingEdges:
            if( n.getName() == dest.getName() ):
                return
        self.edges[src].append((dest, cost))
    def childrenOf(self, node):
        if node in self.edges:
            return list(self.edges[node].items())
        else:
            return []
    def hasNode(self, node):
        return node in self.nodes
    def __str__(self):
        result = ''
        for src in self.nodes:
            for dest in self.edges[src]:
                result = result + src.getName() + '-> ('\
                + dest[0].getName() + ',' + str(dest[1]) + ')\n'
        return result
    
class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource(), edge.getCost())
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



def DFS(graph, start, end, path, shortest, cost=0, allPaths={}):
    """
    Requires:
    graph a Digraph;
    start and end nodes;
    path and shortest lists of nodes
    Ensures:
    a shortest path from start to end in graph
    """
    path = path + [start]
    print('Current DFS path:', printPath(path), 'TC:', cost)
    if start == end:
        return (path, allPaths)
    

    for (edge, edgeCost) in graph.childrenOf(start):
        if edge not in path: #avoid cycles
            pathCost = cost + edgeCost
            if shortest == None or len(path) < len(shortest):
                (newPath, allPaths) = DFS(graph, edge, end, path, shortest, pathCost, allPaths)
                if newPath != None:
                    if str(newPath) not in allPaths :
                        allPaths[str(newPath)] = (newPath, pathCost)
                    pathCost = cost - edgeCost
                    shortest = newPath
    return (shortest, allPaths)

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
    (shortest, allPaths) = DFS(graph, start, end, [], None)
    return (shortest, allPaths)



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
    g.addEdge(Edge(nodes[0],nodes[1], 1))
    g.addEdge(Edge(nodes[1],nodes[2], 10))
    g.addEdge(Edge(nodes[2],nodes[3], 1))
    g.addEdge(Edge(nodes[2],nodes[4], 100))
    g.addEdge(Edge(nodes[3],nodes[4], 1))
    g.addEdge(Edge(nodes[3],nodes[5], 1))
    g.addEdge(Edge(nodes[0],nodes[2], 1))
    g.addEdge(Edge(nodes[1],nodes[0], 1000))
    g.addEdge(Edge(nodes[3],nodes[1], 1))
    g.addEdge(Edge(nodes[4],nodes[0], 1))

    print(g)
    (shortest, allPaths) = search(g, nodes[0], nodes[5])
    print('Shortest path found by DFS:', printPath(shortest))

    for key in allPaths.keys():
        print('Path:', printPath(allPaths[key][0]), " with cost ", allPaths[key][1])    

testSP()

    
    
