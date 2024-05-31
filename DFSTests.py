# 2023-2024 Programacao 2 LTI
# Grupo 42
# 60253 Hugo Silva
# 60232 DUarte Correia
import random
import unittest
from depthFirstSearchInGraphCap122 import *

class TestDigraph(unittest.TestCase):
    NUMBER_OF_NODES = 15
    def setUp(self):
        self.graph = Digraph()
        self.testNodes = []
        for i in range(1, self.NUMBER_OF_NODES+1): 
            node = Node('N_'+str(i))
            self.testNodes.append(node)
            self.graph.addNode(node)


    def test_addNode(self):
        node1 = self.testNodes[random.randint(0, self.NUMBER_OF_NODES-1)]
        node2 = self.testNodes[random.randint(0, self.NUMBER_OF_NODES-1)]
        node3 = self.testNodes[random.randint(0, self.NUMBER_OF_NODES-1)]

        self.assertEqual(len(self.graph.nodes), self.NUMBER_OF_NODES)
        self.assertIn(node1, self.graph.nodes)
        self.assertIn(node2, self.graph.nodes)
        self.assertIn(node3, self.graph.nodes)
        self.assertFalse(self.graph.hasNode(Node("NON_EXISTING_NODE")))

    def test_addEdge(self):
        node1 = self.testNodes[random.randint(0, self.NUMBER_OF_NODES-1)]
        node2 = self.testNodes[random.randint(0, self.NUMBER_OF_NODES-1)]
        node3 = self.testNodes[random.randint(0, self.NUMBER_OF_NODES-1)]
        # Ensure that the graph edges are empty for the test nodes
        self.graph.edges[node1] = []
        self.graph.edges[node2] = []
        self.graph.edges[node3] = []

        try :
            self.graph.addEdge(Edge(node1, node2, 1))
            self.graph.addEdge(Edge(node2, node3, 2))
            self.assertEqual(len(self.graph.edges[node1]), 1)
            self.assertEqual(len(self.graph.edges[node2]), 1)
            self.assertEqual(len(self.graph.edges[node3]), 0)
            self.assertIn((node2, 1), self.graph.edges[node1])
            self.assertIn((node3, 2), self.graph.edges[node2])

            self.assertEqual(self.graph.childrenOf(node1), [(node2, 1)])
            self.assertEqual(self.graph.childrenOf(node2), [(node3, 2)])
            self.assertEqual(self.graph.childrenOf(node3), [])
        finally:
            # Clean up. Ensure that the graph edges are empty for the test nodes
            self.graph.edges = {}

    def test_childrenOf(self):
        # Testing of this method is done in test_addEdge
        pass
    
    def test_hasNode(self):
        node1 = self.testNodes[random.randint(0, self.NUMBER_OF_NODES-1)]
        node2 = self.testNodes[random.randint(0, self.NUMBER_OF_NODES-1)]
        node3 = self.testNodes[random.randint(0, self.NUMBER_OF_NODES-1)]
        self.assertTrue(self.graph.hasNode(node1) != [])
        self.assertTrue(self.graph.hasNode(node2) != [])
        self.assertTrue(self.graph.hasNode(node3) != [])
        self.assertFalse(self.graph.hasNode(Node("NON_EXISTING_NODE")) == [])

    def test_str(self):
        aGraph = Digraph()
        nodeA = Node('A')
        nodeB = Node('B')
        nodeC = Node('C')
        aGraph.addNode(nodeA)
        aGraph.addNode(nodeB)
        aGraph.addNode(nodeC)
        
        aGraph.addEdge(Edge(nodeA, nodeB, 1))
        aGraph.addEdge(Edge(nodeB, nodeC, 2))
        expected_output = "A-> (B,1)\nB-> (C,2)\n"
        self.assertEqual(str(aGraph), expected_output)

    def test_search(self):
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

        (shortest, allPaths) = search(g, nodes[0], nodes[5])        

        self.assertEqual(shortest, [nodes[0], nodes[2], nodes[3], nodes[5]])
        self.assertIsInstance(allPaths, dict)
        self.assertEqual(len(allPaths), 2) # Two paths found
        for pathKey in allPaths.keys():
            self.assertIsInstance(allPaths[pathKey], tuple)
            self.assertIsInstance(allPaths[pathKey][0], list)
            self.assertIsInstance(allPaths[pathKey][1], int)
            # Ensure to find two paths 1- [nodes[0], nodes[2], nodes[3], nodes[5]] and 2 - [nodes[0], [nodes[1], nodes[2], nodes[3], nodes[5]]
            if( printPath(allPaths[pathKey][0]) != printPath([nodes[0], nodes[2], nodes[3], nodes[5]]) and printPath(allPaths[pathKey][0]) != printPath([nodes[0], nodes[1], nodes[2], nodes[3], nodes[5]]) ):
                self.assertTrue(False, "The paths found are not the expected ones")


if __name__ == "__main__":
    unittest.main()