def minimumPassesOfMatrix(matrix):
    # Write your code here.
    passes= convertNegatives(matrix)
	return passes-1 if not containsNegative(matrix) else -1

def convertNegatives(matrix):
	q=getPositivePos(matrix)
	passes=0
	while q:
		size=len(q)
		while size>0:
			currentRow,currentCol=q.pop(0)
			
			adjecent=FindAdj(currentRow,currentCol,matrix)
			for x in adjecent:
				row,col=x
				val=matrix[row][col]
				if val<0:
					matrix[row][col]*=-1
					q.append([row,col])
			size-=1
		passes+=1
		
	return passes

def getPositivePos(matrix):
	pos=[]
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if matrix[i][j]>0:
				pos.append([i,j])
	return pos

def FindAdj(row,col,matrix):
	adj=[]
	if row>0:
		adj.append([row-1,col])
	if row<len(matrix)-1:
		adj.append([row+1,col])
	if col>0:
		adj.append([row,col-1])
	if col<len(matrix[0])-1:
		adj.append([row,col+1])
	return adj

def containsNegative(matrix):
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if matrix[i][j]<0:
				return True
	return False