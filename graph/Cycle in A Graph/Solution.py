def cycleInGraph(edges):
    # Write your code here.
    visited=[0]*len(edges)
	currentlyInStack=[0]*len(edges)
	
	for i in range(len(edges)):
		if visited[i]==1:
			continue
		containsCycle = isCyclic(i,edges,visited,currentlyInStack)
		if containsCycle:
			return True
	return False

def isCyclic(node,edges,visited,currentlyInStack):
	visited[node]=1
	currentlyInStack[node]=1
	
	for neigh in edges[node]:
		if visited[neigh]==0:
			containsCycle = isCyclic(neigh,edges,visited,currentlyInStack)
			if containsCycle:
				return True
		elif currentlyInStack[neigh]==1:
			return True
	currentlyInStack[node]=False
	return False