times = int( input() )

for i in range( times ):
    x = input()
    print("Sum of all digits of",x,"is",sum(list(map(int,list(x)))))
    

'''
for i in range( times ):
    x = input()
    total = 0
    for j in range(len(x)):
        total += int( x[j] )
    print("Sum of all digits of",x,"is",total)
'''
