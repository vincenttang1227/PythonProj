userInput = input()

total = 0
for i in range( len(userInput) ):
    total += ord(userInput[i])
    print("ASCII code for '{:s}' is {:d}".format(userInput[i],ord(userInput[i])))
print(total)
