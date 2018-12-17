list1=[]
for i in range(9):
    list1.append( int(input()) )

maxNum = max(list1)
maxIndex = list1.index( maxNum )
print("Index of the largest number {:d} is: ({:d}, {:d})".format(maxNum, maxIndex//3, maxIndex%3 ))
minNum = min(list1)
minIndex = list1.index( minNum )
print("Index of the smallest number {:d} is: ({:d}, {:d})".format(minNum, minIndex//3, minIndex%3))
