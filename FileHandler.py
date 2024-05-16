import stations as stations
import depthFirstSearchInGraphCap122 as dfs

class FileHandler:
    def __init__(self):
        pass
    
    
    
    def readFileConections(self, file_name):
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
        
    def readFileNetwork(self, file_name):
        """
        Requires: file_name is a string with the name of the file
        Ensures: creates a makes the filter of every line of the file, creates a STATION object 
                add those objects to a list used to create the network object that is returned
        """
        file = open(file_name, 'r')
        networkList = []
        for line in file:
            line = line.strip()
            line = line.split('[')
            line1 = line[0]
            line2 = line[1]
            line2 = "[" + line2
            line1 = line1.split(', ')
            line1 = line1[:-1]
            connectionedList = FileHandler().getConnectionsList(line2)
            lineList = line1 + [connectionedList]
            station = stations.Station(lineList[0], lineList[1], lineList[2])
            networkList.append(station)
        network = stations.Network(networkList)     
        file.close()
        return network
    
    
    def getConnectionsList(self, stringListOfConnecctions): 
        listOfConnections = stringListOfConnecctions

        # remove '[(' and ')]' from the string
        listOfConnections = listOfConnections.replace('[(', '')
        listOfConnections = listOfConnections.replace(')]', '')

        # split the string in the commas
        listOfConnections = listOfConnections.split('), (')

        connections = []
        for i in range(len(listOfConnections)):
            connection = listOfConnections[i].split(', ')
            connectionTupple = (connection[0], int(connection[1]))
            connections.append(connectionTupple)

        return connections


 
        




