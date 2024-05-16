
def getConnectionsList(stringListOfConnecctions): 
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

listOfConnections = "[(R, 15), (M, 8), (B, 12)]"

conns = getConnectionsList(listOfConnections)
print(conns[0])