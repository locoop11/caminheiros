import unittest
import depthFirstSearchInGraphCap122 as dfs
from stations import *
from FileHandler import FileHandler

class  TestNetwork(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.validNetworkTestFileName = './tests/myLevadasNetwork.txt'
        self.validNetwork = None
        try:
            self.validNetwork = FileHandler().readFileNetwork(self.validNetworkTestFileName)
        except Exception as e:
            errorMessage = f"Error: {str(e)}"
            self.assertFalse(True, "An error occurred while invoking FileHandler().readFileNetwork with test file " + self.validNetworkTestFileName + ". " + errorMessage)
    
    def test_readResultIsANetwork(self):
        network = self.validNetwork
        # network should be a Network object
        self.assertTrue(isinstance(network, Network), "The result of FileHandler().readFileNetwork is not of type stations.Network")

    def test_networkIsAList(self):    
        network = self.validNetwork
        # network.get_network() is a list
        self.assertTrue(isinstance(network.get_network(), list), "The result of FileHandler().readFileNetwork is not a list")

    def test_networkIsListOfStations(self):
        network = self.validNetwork
        # assert that elements of network.get_network() are of type stations.Station
        self.assertTrue(all(isinstance(station, Station) for station in network.get_network()), "Elements of the result list of FileHandler().readFileNetwork are not of type stations.Station")
        
    def test_networkHasAllStations(self):
        network = self.validNetwork
        # assert that the network has all the stations
        message = "The return of FileHandler().readFileNetwork number of stations is not as expected. Expected 7, got" + str(len(network.get_network()))
        self.assertEqual(len(network.get_network()), 4, message)

    def test_NetworkIsAsExpected(self):
        network = self.validNetwork
        # assert that the network is as expected
        station0 = network.get_network()[0]
        
        self.assertEqual(station0.get_id(), 'A', "The first station id is not as expected")
        self.assertEqual(station0.get_name(), 'Seixal', "The first station name is not as expected")

    def test_NetworksStationsIsCorrectlyConvertedAsString(self):
        network = self.validNetwork
        # assert that the network is as expected
        station0 = network.get_network()[0]
        self.assertEqual(str(station0), 'A, Seixal, [(D, 15), (C, 8), (B, 12)]', "The first station id is not as expected when converted to String")
       
    def test_outOfNetwork(self):
        network = self.validNetwork
        print(network.get_network())
        connection = Connection('Ponta do Pargo', 'Queimadas', network)
        k = 3
        bestPaths = network.getBestPaths(connection, k)
        #Assert that bestPaths returns a list with one element that is a string saying that the connection is out of the network   
        self.assertEqual(bestPaths[0], "Ponta do Pargo out of the network", "Unexpected optimal path")

        connection2 = Connection('XPTO', 'XPTO2', network)
        bestPaths = network.getBestPaths(connection2, k)
        self.assertEqual(bestPaths[0], "XPTO and XPTO2 out of the network", "Unexpected optimal path")
        
    def test_getBestPaths(self):
        network = self.validNetwork
        print(network.get_network())
        connection = Connection('Donta do Pargo', 'Queimadas', network)
        k = 3
        bestPaths = network.getBestPaths(connection, k)
        # Assert that we find only one network with cost 30
        self.assertEqual(len(bestPaths), 1, "The number of best paths is not as expected")
        self.assertEqual(bestPaths[0][1], 30, "The cost of the best path is not as expected")
        # assert that the path found is DAC
        self.assertEqual(dfs.printPath((bestPaths[0][0])), "D->A->C", "The best path is not as expected")

    def test_connectionNotInNetwork(self):
        network = self.validNetwork
        connection = Connection('Porto', 'Lisboa', network)
        k = 3
        bestPaths = network.getBestPaths(connection, k)
        #Assert that bestPaths returns a list with one element that is a string saying that the connection is out of the network
        self.assertEqual(len(bestPaths), 1, "The number of best paths is not as expected")
        self.assertEqual(bestPaths[0], "Porto and Lisboa out of the network", "The best path is not as expected should be 'Porto and Lisboa out of the network'")
        connection2 = Connection('Porto', 'Queimadas', network)
        k = 3
        bestPaths = network.getBestPaths(connection2, k)
        #Assert that bestPaths returns a list with one element that is a string saying that the connection is out of the network
        self.assertEqual(len(bestPaths), 1, "The number of best paths is not as expected")
        self.assertEqual(bestPaths[0], "Porto out of the network", "The best path is not as expected should be 'Porto out of the network'")
        connection3 = Connection('Queimadas', 'Lisboa', network)
        k = 3
        bestPaths = network.getBestPaths(connection3, k)
        #Assert that bestPaths returns a list with one element that is a string saying that the connection is out of the network
        self.assertEqual(len(bestPaths), 1, "The number of best paths is not as as expected")
        self.assertEqual(bestPaths[0], "Lisboa out of the network", "The best path is not as expected should be 'Porto out of the network'")
    def teste_ConnectionEmpyConnection(self):
        network = self.validNetwork
        connection = Connection(None, None, network)
        k = 3
        with self.assertRaises(ValueError):
            network.getBestPaths(connection, k)



    


        
    
        


if __name__ == '__main__':
    unittest.main()