import unittest
import depthFirstSearchInGraphCap122 as dfs
from stations import *
from FileHandler import FileHandler



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

nonExistingStationId = "nonexistingStationId"

class TestConnections(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.validConnectionsTestFileName = './tests/myStations.txt'
        self.validConnections = None

        try:
            self.validConnections = FileHandler().readFileConnections(self.validConnectionsTestFileName)
        except Exception as e:
            errorMessage = f"Error: {str(e)}"
            self.assertTrue(False, "An error occurred while invoking FileHandler().readFileConnections with test file " + self.validConnectionsTestFileName + ". " + errorMessage)
    
    def test_connectionsIsConnectionsList(self):
        # conn_list should be a list
        self.assertTrue(isinstance(self.validConnections, ConnectionsList), "The result of FileHandler().readFileConnections is not a ConnectionsList")

    def test_connectionsIsListOfConnections(self):
        # assert that elements of conn_list are of type stations.Connection
        self.assertTrue(all(isinstance(conn, Connection) for conn in self.validConnections.get_connections()), "Elements of the result list of FileHandler().readFileConnections are not of type stations.Connection")

    def test_connectionsReadAllConnections(self):
        message = "The return of FileHandler().readFileConnections number of connections is not as expected. Expected 5, got" + str(len(self.validConnections.get_connections()))
        self.assertEqual(len(self.validConnections.get_connections()), 5, message)

    def test_connectionsIsAsExpected(self):
        # assert that the connections are as expected
        self.assertEqual(str(self.validConnections.get_connections()[0]), "(Cedro, Queimada)", "The first connection is not as expected")


class TestStation(unittest.TestCase):
    def setUp(self):
        self.stationWithNonExistingLink = Station(stationA[0], stationA[1], stationA[2] + 
                            [(nonExistingStationId, 15)])
        self.stationEmpty = Station(stationA[0], stationA[1], [])

    def test_get_id(self):
        self.assertEqual(self.stationWithNonExistingLink.get_id(), stationA[0])
        self.assertEqual(self.stationEmpty.get_id(), stationA[0])

    def test_get_name(self):
        self.assertEqual(self.stationWithNonExistingLink.get_name(), stationA[1])
        self.assertEqual(self.stationEmpty.get_name(), stationA[1])

    def test_get_connected(self):
        nonExistingStationId = "nonexistingStationId"
        self.assertEqual(self.stationWithNonExistingLink.get_connectedStringsList(), stationA[2]+ [(nonExistingStationId, 15)])

        self.assertEqual(self.stationEmpty.get_connectedStringsList(), [], self.stationEmpty.get_connectedStringsList())


if __name__ == '__main__':
    unittest.main()