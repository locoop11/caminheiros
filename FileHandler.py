import stations as stations
import depthFirstSearchInGraphCap122 as dfs

class FileHandler:
    def __init__(self):
        pass
    
    
    
    def readFileConections(file_name):
        """
        Requires: file_name is a string with the name of the file
        Ensures: a list of objects of class Connections
        """
        file = open(file_name, 'r')
        connections = stations.ConnectionsList([])
        for line in file:
            line = line.strip()
            line = line.split(' - ')
            connection = stations.Connection(line[0], line[1])
            connections.add_connection(connection)
        file.close()
        return connections
        


    def readFileNetwork(file_name):
        """
        Requires: file_name is a string with the name of the file
        Ensures: a list of objects of class stationNetwork
        """
        file = open(file_name, 'r')
        network = stations.Network([])
        for line in file:
            line = line.strip()
            line = line.split(' - ')
            station = stations.Station(line[0], line[1], line[2])
            network.add_station(station)
        file.close()
        return network





