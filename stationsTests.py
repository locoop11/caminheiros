import unittest
import depthFirstSearchInGraphCap122 as dfs
from stations import *



stationA = ['A', 'Seixal', [('R', 15), ('M', 8), ('B', 12)]]
stationB = ['B', 'Porto Moniz', [('A', 12), ('S', 10)]]
stationC = ['C', 'Pico Ruivo', [('GJ', 32), ('I', 5)]]
stationD = ['D', 'Queimadas', [('Z', 18), ('AC', 11)]]
stationE = ['E', 'Ponta do Pargo', [('DW', 13)]]
stationM = ['M', 'Sao Vicente', [('A', 8), ('S', 5)]]
stationGJ = ['GJ', 'Santana', [('C', 32), ('I', 5)]]
stationR = ['R', 'Ribeira Brava', [('A', 15), ('S', 10)]]
stationS = ['S', 'Sao Vicente', [('M', 5), ('R', 10)]]
stationI = ['I', 'Santana', [('C', 5), ('GJ', 5)]]
stationZ = ['Z', 'Santana', [('D', 18), ('A', 11)]]
stationDW = ['DW', 'Calheta', [('E', 13)]]


testDataA = [['A', 'Seixal', [('R', 15), ('M', 8), ('B', 12)]],
             ['C', 'Pico Ruivo', [('GJ', 32), ('I', 5)]],
             ['D', 'Queimadas', [('Z', 18), ('AC', 11)]],
             ['E', 'Ponta do Pargo', [('DW', 13)]]]


class TestConnection(unittest.TestCase):
    def setUp(self):
        self.conn = Connection("Start", "Destination")

    def test_get_nameStarting(self):
        self.assertEqual(self.conn.get_nameStarting(), "Start")

    def test_get_nameDestination(self):
        self.assertEqual(self.conn.get_nameDestination(), "Destination")

class TestConnectionsList(unittest.TestCase):
    def setUp(self):
        self.conn_list = ConnectionsList([])

    def test_add_connection(self):
        self.conn_list.add_connection(Connection("Start", "Destination"))
        self.assertEqual(len(self.conn_list.get_connections()), 1)

class TestStation(unittest.TestCase):
    def setUp(self):
        self.stationWithNonExistingLink = Station(stationA[0], stationA[1], stationA[2] + 
                            [('nonexistingStationId', 15)])
        self.stationEmpty = Station(stationA[0], stationA[1], [])

    def test_get_id(self):
        self.assertEqual(self.stationWithNonExistingLink.get_id(), stationA[0])
        self.assertEqual(self.stationEmpty.get_id(), stationA[0])

    def test_get_name(self):
        self.assertEqual(self.stationWithNonExistingLink.get_name(), stationA[1])
        self.assertEqual(self.stationEmpty.get_name(), stationA[1])

    def test_get_connected(self):
        self.assertEqual(self.stationWithNonExistingLink.get_connected(), stationA[2]+ [('nonexistingStationId', 15)])
        self.assertEqual(self.stationEmpty.get_connected(), [])

class TestNetwork(unittest.TestCase):
    def setUp(self):
        self.network = Network([])

    def test_add_station(self):
        self.network.add_station(Station(1, "Station1", "Station2"))
        self.assertEqual(len(self.network.get_network()), 1)

    def test_getBestPath(self):
        pass

if __name__ == '__main__':
    unittest.main()