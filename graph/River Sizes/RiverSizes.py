def riverSizes(matrix):
    # Write your code here.
	if not matrix:
		return []
	sizes=[]
	visited=[[False for values in row] for row in matrix]
	
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if visited[i][j]:
				continue
			getSize(i,j,visited,matrix,sizes)
	return sizes

def getSize(i,j,visited,matrix,sizes):
	currentRiverSize=0
	nodesToExplore=[[i,j]]
	while nodesToExplore:
		currentNode=nodesToExplore.pop()
		x,y=currentNode
		if visited[x][y]:
			continue
		visited[x][y]=True
		if matrix[x][y]==0:
			continue
		currentRiverSize+=1
		unvisitedNeighbours=getNeighbours(x,y,visited,matrix)
		for nodes in unvisitedNeighbours:
			nodesToExplore.append(nodes)
	if currentRiverSize>0:
		sizes.append(currentRiverSize)

def getNeighbours(i,j,visited,matrix):
	toReturn =[]
	if i>0 and not visited[i-1][j]:
		toReturn.append([i-1,j])
	if i<len(matrix)-1 and not visited[i+1][j]:
		toReturn.append([i+1,j])
	if j>0 and not visited[i][j-1]:
		toReturn.append([i,j-1])
	if j<len(matrix[0])-1 and not visited[i][j+1]:
		toReturn.append([i,j+1])
	return toReturn