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
        return self.nameStarting + " -> " + self.nameDestination
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
        return self.__str__()
    def __repr__(self):
        return self.__str__()



class Station (object):
    def __init__(self, id, name, connected):
        self.id = id
        self.name = name
        self.connected = connected  
        



    def get_id(self):
        return self.id
    def get_name(self):
        return self.name
    def get_connected(self):
        return self.connected
    def __str__(self):
        return self.__str__()
    

class Networok (object):
    def __init__(self, network):
        self.network = network
        self.graph = self.createGraph()

    def add_station(self, station):
        self.network.append(station)
    
    
    def createGraph(self):
        graph = dfs.Graph()
        for station in self.network:
            node = dfs.Node(station.get_name())
            graph.addNode(node)
            connected = station.get_connected().split('),')
            for i in connected:
                edge = dfs.Edge(node, dfs.Node(i))
                graph.addEdge(edge)
        return graph
    
    def getBestPath(self, connection):
        """
        return (time, path)
        """

        if (connection.get_nameStarting() not in self.network):
            raise ValueError(connection.get_nameStarting() + ' out of the network')
        if (connection.get_nameDestination() not in self.network):
            raise ValueError(connection.get_nameDestination + ' out of the network')
        

        dfs.search(self.graph, connection.get_nameStarting(), connection.get_nameDestination())
    
    
    def get_network(self):
        return self.network
    def __str__(self):
        return self.__str__()
    


