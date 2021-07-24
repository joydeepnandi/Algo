'''
array = [
  [1,  3,  4, 10],
  [2,  5,  9, 11],
  [6,  8, 12, 15],
  [7, 13, 14, 16],
]
Sample Output
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
'''


def zigzagTraverse(array):
    # Write your code here.
	height=len(array)-1
	width=len(array[0])-1
	row=0
	col=0
	result=[]
	goingdown=True
	
	while not outofbounds(height,width,row,col):
		result.append(array[row][col])
		if goingdown:
			if row==height or col==0:
				goingdown=False
				if row==height:
					col+=1
				else:
					row+=1
			else:
				col-=1
				row+=1
		else:
			if row==0 or col==width:
				goingdown=True
				if col==width:
					row+=1
				else:
					col+=1
			else:
				col+=1
				row-=1
	return result

def outofbounds(height,width,row,col):
	return row<0 or row>height or col>width or col<0
