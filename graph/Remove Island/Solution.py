def removeIslands(matrix):
    # Write your code here.
    #traverse through the boundaries and change all 1's and dfs to 2
	#traverse through the matrix and change all 1 to 0
	#change all 2 to 1
	
	if not matrix:
		return []
	m=len(matrix)
	n=len(matrix[0])
	
	for i in range(0,m):
		dfs(i,0,matrix)
		dfs(i,n-1,matrix)
	
	for j in range(0,n):
		dfs(0,j,matrix)
		dfs(m-1,j,matrix)
	
	for i in range(m):
		for j in range(n):
			if matrix[i][j]==2:
				matrix[i][j]=1
			elif matrix[i][j]==1:
				matrix[i][j]=0
	return matrix

def dfs(i,j,matrix):
	if i<0 or j<0 or i>=len(matrix) or j>=len(matrix[0]) or matrix[i][j]==0:
		return 
	matrix[i][j]=2
	nx=[0,0,-1,1]
	ny=[1,-1,0,0]
	
	for idx in range(4):
		dfs(i+nx[idx],j+ny[idx],matrix)
	