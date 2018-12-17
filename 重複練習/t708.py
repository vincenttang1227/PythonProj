dic = {}

def inputDict():
    k = input("Key: ")
    while k != 'end':
        dic[k]= input("Value: ")
        k = input("Key: ")

print("Create dict1:")
inputDict()
print("Create dict2:")
inputDict()

for i in sorted(dic.keys()):
    print(i,": ",dic[i],sep="")
