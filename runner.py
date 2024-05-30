import FileHandler as fh
import stations as stations
import depthFirstSearchInGraphCap122 as dfs


class runner ():
    def __innit__(self, networkFileName, connectionsFileName, resultFileName, k):
        self.networkFileName = networkFileName
        self.connectionsFileName = connectionsFileName
        self.resultFileName = resultFileName
        self.k = k

        #TODO: Verificar se os ficheiros existem caso contrario raise exception
    

    def run(self):
        FileHandler = fh.FileHandler()
        connections = FileHandler.readFileConnections(self.connectionsFileName)
        network = FileHandler.readFileNetwork(self.networkFileName)

        dicBestConnections = {}
        for conn in connections:
            bestPath = network.getBestPath(conn, self.k)
            dicBestConnections[conn] = bestPath

        FileHandler.saveBestResults(self.resultFileName, dicBestConnections)

        
        
            


        
        