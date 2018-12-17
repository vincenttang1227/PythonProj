'''
x = input()

for i in range(-1,-len(x)-1,-1):
    print(x[i],end="")
'''

a = list( input() )
a.reverse()
print(''.join(a))
