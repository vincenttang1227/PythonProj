def compute(x, y):
    if y == 0:
        return x
    else:
        return compute(y, x%y)

data = input().split(',')
data = list( map(int, data) )
print( compute(data[0], data[1]) )
