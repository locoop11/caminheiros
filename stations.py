import depthFirstSearchInGraphCap122 as dfs

class Connection (object):
    def __init__(self, nameStarting, nameDestination, associatedNetwork):
        self.stationStarting = self.transformToStation(nameStarting, associatedNetwork)
        self.stationDestination = self.transformToStation(nameDestination, associatedNetwork)
        self.associatedNetwork = associatedNetwork
        self.nameStartingString = nameStarting
        self.nameDestinationString = nameDestination
        

    
    
    def transformToStation(self, name, associatedNetwork):
        for station in associatedNetwork.get_network():
            if station.get_name() == name:
                return station
         


    def get_nameStartingString(self):
        return self.nameStartingString
    def get_nameDestinationString(self):
        return self.nameDestinationString
    def get_stationStarting(self):
        return self.stationStarting
    def get_stationDestination(self):
        return self.stationDestination
    def __str__(self):
        return "(" + self.get_nameStartingString() +(", ")+ self.get_nameDestinationString() + ")"
    
class ConnectionsList (object):
    def __init__(self, connections):
        self.connections = connections
    def add_connection(self, connection):
        self.connections.append(connection)
    def get_connections(self):
        return self.connections
    def __str__(self):
        return '\n'.join(str(connection) for connection in self.connections)


class Station (object):
    """
    station is a object with caracteristics, id, name, list of connected stations and itself node object thats is 
    only atributed when the station Node is created in the graph object
    """
    def __init__(self, id, name, connectedSrtingsList):
        self.id = id
        self.name = name
        self.connectedStringsList = connectedSrtingsList
        self.node = dfs.Node(id) 
        self.connectedNodesCostList = [] 


    def createconnectedNodesCostList(self, stationsList):
        """
        Creates a list of lists thats it is, (a list of [node, time]) that are connected to the station by having in mind all the existing stations,
        this stationList is a list of all the object stations that will be used in the network object

        """
        for connectedString in self.connectedStringsList:
            for station in stationsList:
                if connectedString[0] == station.get_id():
                    self.connectedNodesCostList.append([station.get_node(), connectedString[1]])
                    break

   

    def get_id(self):
        return self.id
    def get_name(self):
        return self.name
    def get_connectedStringsList(self):
        return self.connectedStringsList
    def get_node(self):
        return self.node
    def get_connectedNodesCostList(self):
        return self.connectedNodesCostList
    def __str__(self):
        return self.id + ", " + self.name + ", " + str(self.connectedStringsList).replace("'", "")
    

class Network (object):
    """network is a list of stations objects"""
    def __init__(self, network):
        self.network = network
        self.graph = self.createGraph()

    def add_station(self, station):
        self.network.append(station)
    
    def getStationById(self, id):
        for station in self.network:
            if station.get_id() == id:
                return station
        return None
    
    def createGraph(self):
        graph = dfs.Graph()
        for station in self.network:
            graph.addNode(station.get_node())
        for station in self.network:
            for connectedNodeCost in station.get_connectedNodesCostList():
                connectedNode = connectedNodeCost[0]
                connectedCost = connectedNodeCost[1]
                edge = dfs.Edge(station.get_node(), connectedNode, connectedCost)
                graph.addEdge(edge)       
        return graph
    
    def getBestPaths(self, connection, k):
        """
        return (time, path)
        """
        startingStation = None
        destinationStation = None
        if connection.get_nameStartingString() == None and connection.get_nameDestinationString() == None:
            raise ValueError("Connection starting point and destination point is empty")
        if connection.get_nameStartingString() == None:
            raise ValueError("Connection starting point is empty")
        if connection.get_nameDestinationString() == None:
            raise ValueError("Connection destination point is empty")

        if connection.get_stationStarting() == None and connection.get_stationDestination() == None:
            orderedPaths = [connection.get_nameStartingString() + " and " + connection.get_nameDestinationString() + " out of the network"]
            return orderedPaths
        if connection.get_stationStarting() == None:
            orderedPaths = [connection.get_nameStartingString() + " out of the network"]
            return orderedPaths
        if connection.get_stationDestination() == None:
            orderedPaths = [connection.get_nameDestinationString() + " out of the network"]
            return orderedPaths

        for station in self.network:
            if station.get_name() == connection.get_stationStarting().get_name():
                startingStation = station
            if station.get_name() == connection.get_stationDestination().get_name():
                destinationStation = station
    
        #assumindo que path sao todos os caminhos possiveis no formato (path, time)
        (shortestPath, allPaths)= dfs.DFS(self.graph, startingStation.get_node(), destinationStation.get_node(), [], None, 0, {})
        paths = []
        for path in allPaths.values():
            paths.append(path)

        orderedPaths = sorted(paths, key=lambda x: x[1])
        
        if k > len(orderedPaths):
            k = len(orderedPaths)
        orderedPaths = orderedPaths[:k]


            

        

        return orderedPaths
            
    
    def get_network(self):
        return self.network
    def __str__(self):
        return str(self.graph)
    


