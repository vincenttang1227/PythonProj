userInput = input().split('-')
validWord = "Valid SSN"
if len(userInput[0]) != 3 or not userInput[0].isdigit():
    validWord = "Invalid SSN"

if len(userInput[1]) != 2 or not userInput[1].isdigit():
    validWord = "Invalid SSN"

if len(userInput[2]) != 4 or not userInput[2].isdigit():
    validWord = "Invalid SSN"

print( validWord )

'''
userInput = input()

if (''.join(userInput.split('-'))).isdigit():
    print("Valid SSN")
else:
    print("Invalid SSN")
'''
