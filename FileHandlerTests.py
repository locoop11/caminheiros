import unittest
import depthFirstSearchInGraphCap122 as dfs
from FileHandler import FileHandler

class TestConnections(unittest.TestCase):
    def setUp(self):
        self.conn_fileName = './tests/myStations.txt'
        self.network_fileName = './tests/myLevadasNetwork.txt'

    def test_readFileConnections(self):
        connectionsFileName = self.conn_fileName
        conn_list = None
        try:
            conn_list = FileHandler().readFileConnections(self.connectionsFileName)
        except Exception as e:
            errorMessage = f"Error: {str(e)}"
            conn_list = []  # Set conn_list to an empty list or handle the error in an appropriate way
            self.assertTrue(False, "An error occurred while invoking FileHandler().readFileConnections with test file " + connectionsFileName + ". " + errorMessage)

        # conn_list shoube be a list
        self.assertTrue(isinstance(conn_list, list), "The result of FileHandler().readFileConnections is not a list")

        message = "The return of FileHandler().readFileConnections number of connections is not as expected. Expected 5, got" + str(len(conn_list))
        self.assertEqual(len(conn_list), 5, message)

        # assert that elements of conn_list are of type stations.Connection
        self.assertTrue(all(isinstance(conn, dfs.Connection) for conn in conn_list), "Elements of the result list of FileHandler().readFileConnections are not of type stations.Connection")

    def test_readFileNetwork(self):
        network_fileName = self.network_fileName
        network = None
        try:
            network = FileHandler().readFileNetwork(network_fileName)
        except Exception as e:
            errorMessage = f"Error: {str(e)}"
            self.assertFalse(True, "An error occurred while invoking FileHandler().readFileNetwork with test file " + network_fileName + ". " + errorMessage)

        # network should be of type stations.Network type
        self.assertTrue(isinstance(network, dfs.Network), "The result of FileHandler().readFileNetwork is not of type stations.Network")
        
if __name__ == '__main__':
    unittest.main()