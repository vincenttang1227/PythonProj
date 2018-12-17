numList = []
countList = []

for i in range(10):
    numList.append( int(input()) )

for i in range(10):
    countList.append( numList.count( numList[i] ) )

print( numList[ countList.index( max( countList ) ) ] )
print( max( countList) )
