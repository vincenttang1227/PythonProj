def converCard( n ):
    if n == 'A':
        return 1
    elif n == 'J':
        return 11
    elif n == 'Q':
        return 12
    elif n == 'K':
        return 13
    else:
        return int(n)

total = 0
for i in range(5):
    total += converCard( input() )

print( total )

'''
card = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13}

total = 0
for i in range(5):
    total += card[input()]

print(total)
'''
