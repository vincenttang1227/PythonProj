a = int( input() )

list1 = []
while a != 9999:
    list1.append(a)
    a = int( input() )

print( min(list1) )
