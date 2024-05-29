import stations as stations
import depthFirstSearchInGraphCap122 as dfs

class FileHandler:
    def __init__(self):
        pass
    
    
    
    def readFileConnections(self, file_name):
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
        stationsList = []
        for line in file:
            line = line.strip()
            line = line.split('[')
            stationIdAndNameString = line[0]
            connectionsString = line[1]
            connectionsString = "[" + connectionsString
            stationIdAndNameString = stationIdAndNameString.split(', ')
            stationIdAndNameString = stationIdAndNameString[:-1]
            #conections work
            connectionedList = FileHandler().getConnectionsList(connectionsString)
            #station work
            stationId = stationIdAndNameString[0]
            stationName = stationIdAndNameString[1]
            station = stations.Station(stationId, stationName, connectionedList)
            stationsList.append(station)
        #create the connectedNodesCostList for every station instead of just having the connectedStringsList
        for station in stationsList:
            station.createconnectedNodesCostList(stationsList)
        #create the network object
        network = stations.Network(stationsList)     
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

    def saveBestResults(self, file_name, dicBestConnections):
        """
        Requires: file_name is a string with the name of the file
        Ensures: a file with the best connections
        """
        file = open(file_name, 'w')
        for key in dicBestConnections:
            file.write(key + ' - ' + str(dicBestConnections[key]) + '\n')
        file.close()
 
        




