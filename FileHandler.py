import stations as stations
import depthFirstSearchInGraphCap122 as dfs

class FileHandler:
    def __init__(self):
        pass
    
    
    
    def readFileConnections(self, file_name, associatedNetwork):
        """
        Requires: file_name is a string with the name of the file
        Ensures: a list of objects of class Connections
        """
        with open(file_name, 'r') as file:
            connections = stations.ConnectionsList([])
            for line in file:
                line = line.strip()
                line = line.split(' - ')
                connection = stations.Connection(line[0], line[1], associatedNetwork)
                connections.add_connection(connection)
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
        if( listOfConnections == '[]' or listOfConnections == '[ ]'):
            return [()]

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

    def saveBestResults(self, file_name, dicBestConnections, network):
        """
        Requires: file_name is a string with the name of the file
        Ensures: a file with the best connections
        """
        file = open(file_name, 'w')
        for conn in dicBestConnections.keys():
            if( not conn.get_stationDestination() or not conn.get_stationStarting() ):
                file.write('# ' + conn.get_nameStartingString() + ' - ' + conn.get_nameDestinationString() + ':\n')
                file.write(dicBestConnections[conn][0] + '\n')
                continue
            else :
                connString = str(conn).replace('(', '').replace(')', '').replace(",", ' -')
                file.write('# ' + connString + ':\n')
            for path in dicBestConnections[conn]:
                if len(path) == 1:
                    file.write(path + '\n')
                else:
                    results = dfs.printNetworkPath(path[0], network).replace('->', ', ')
                    file.write(str(path[1]) + ', ' + results + '\n')
        file.close()

 
        




