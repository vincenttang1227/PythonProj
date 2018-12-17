def listCreate():
    temp = []
    a = int( input() )
    while a != -9999:
        temp.append( a )
        a = int( input() )
    return temp

print("Create tuple1:")
tuple1 = tuple(listCreate())
print("Create tuple2:")
tuple2 = tuple(listCreate())
print("Combined tuple before sorting:",tuple1+tuple2)
print("Combined list after sorting:",sorted(list(tuple1+tuple2)))
