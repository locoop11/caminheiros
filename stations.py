import depthFirstSearchInGraphCap122 as dfs

class Connection (object):
    def __init__(self, nameStarting, nameDestination):
        self.nameStarting = nameStarting
        self.nameDestination = nameDestination
        
    def get_nameStarting(self):
        return self.nameStarting
    def get_nameDestination(self):
        return self.nameDestination
    def __str__(self):
        return "(" + self.nameStarting +(", ")+ self.nameDestination + ")"
    def __repr__(self):
        return self.__str__()
    
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
        return self.__str__()
    

class Network (object):
    """network is a list of stations objects"""
    def __init__(self, network):
        self.network = network
        self.graph = self.createGraph()

    def add_station(self, station):
        self.network.append(station)
    
    
    def createGraph(self):
        graph = dfs.Graph()
        for station in self.network:
            graph.addNode(station.get_node())
            for connectedNodeCost in station.get_connectedNodesCostList():
                connectedNode = connectedNodeCost[0]
                connectedCost = connectedNodeCost[1]
                edge = dfs.Edge(station.get_node(), connectedNode, connectedCost)
                graph.addEdge(edge)       
        return graph
    
    def getBestPaths(self, connection):
        """
        return (time, path)
        """
        starting_station = None
        destination_station = None

        for station in self.network:
            if station.get_name() == connection.get_nameStarting():
                starting_station = station
            if station.get_name() == connection.get_nameDestination():
                destination_station = station
        if starting_station == None:
            raise ValueError(connection.get_nameStarting() + ' out of the network')
        if destination_station == None:
            raise ValueError(connection.get_nameDestination + ' out of the network')

        paths = dfs.DFS(starting_station.get_node(), destination_station.get_node(), 3)
        
        orderedPaths = sorted(paths, key=lambda x: x[1])
        
        

            

        

        return orderedPaths
            
    
    


    def get_network(self):
        return self.network
    def __str__(self):
        return self.__str__()
    


