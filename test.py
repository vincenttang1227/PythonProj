nameDict = {}

dictKey = input('Key: ')
while dictKey != 'end':
    dictValue = input('Value: ')
    nameDict[dictKey] = dictValue
    dictKey = input('Key: ')
    
print (input('Search key: ') in nameDict)