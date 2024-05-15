import depthFirstSearchInGraphCap122 as dfs
import stations as stations
import FileHandler as fh





def search(, file_name_network, origin, destination):
    """
    Requires: file_name_stations and file_name_network are strings with the name of the files
    origin and destination are strings with the names of the stations
    Ensures: the path from origin to destination
    """
    connections = fh.readFileStations(file_name_stations)
    network = fh.readFileNetwork(file_name_network)
    digraph = fh.createDigraph(network)
    path = dfs.depthFirstSearch(digraph, origin, destination)
    return path




