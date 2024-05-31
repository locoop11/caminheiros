import FileHandler as fh
import stations as stations
import depthFirstSearchInGraphCap122 as dfs


class Runner ():
    def __init__(self, networkFileName, connectionsFileName, resultFileName, k):
        self.networkFileName = networkFileName
        self.connectionsFileName = connectionsFileName
        self.resultFileName = resultFileName
        self.k = k

        #TODO: Verificar se os ficheiros existem caso contrario raise exception
    

    def run(self):
        FileHandler = fh.FileHandler()
        network = FileHandler.readFileNetwork(self.networkFileName)
        connections = FileHandler.readFileConnections(self.connectionsFileName, network)
        

        dicBestConnections = {}
        for conn in connections.get_connections():
            bestPath = network.getBestPaths(conn, self.k)
            dicBestConnections[conn] = bestPath

        FileHandler.saveBestResults(self.resultFileName, dicBestConnections, network)

        
        
            
if __name__ == "__main__":
    runner = Runner('tests/myLevadasNetwork.txt', 'tests/myStations.txt', 'myResults.txt', 3)
    runner.run()
    


        
        