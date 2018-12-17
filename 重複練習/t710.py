dic = {}

k = input("Key: ")
while k != 'end':
    dic[k] = input("Value: ")
    k = input("Key: ")

print( input("Search key: ") in dic.keys() )
