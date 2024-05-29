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
        
        self.assertEqual(str(station0), 'A, Seixal, [(R, 15), (M, 8), (B, 12)]', "The first station id is not as expected when converted to String")
       

if __name__ == '__main__':
    unittest.main()