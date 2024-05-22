import FileHandler as fh
import stations as stations
import depthFirstSearchInGraphCap122 as dfs
import search as search


class runner ():
    def __innit__(self, networkFileName, connectionsFileName, resultFileName):
        self.networkFileName = networkFileName
        self.connectionsFileName = connectionsFileName
        self.resultFileName = resultFileName

        #TODO: Verificar se os ficheiros existem caso contrario raise exception
    

    def run(self):
        FileHandler = fh.FileHandler()
        connections = FileHandler.readFileConections(self.connectionsFileName)
        network = FileHandler.readFileNetwork(self.networkFileName)
        network.createGraph()

        dicBestConnections = {}
        for conn in connections:
            bestConnections = network.getBestPath(conn)
            dicBestConnections[conn] = bestConnections

        FileHandler.saveBestResults(self.resultsFileName, dicBestConnections)

        
        
            


        
        