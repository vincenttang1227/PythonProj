a = int( input() )
b = int( input() )

total = 0
for i in range (a, b+1):
    if i % 2 == 0:
        total += i

print(total)
