numLi = []
countLi = []

for i in range(10):
    numLi.append( int(input()) )

for i in range(10):
    countLi.append( numLi.count( numLi[i] ) )

print( numLi[ countLi.index( max( countLi ) ) ] )
print( max( countList) )
