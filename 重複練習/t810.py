times = int( input() )

for i in range(times):
    list1 = list( map(float, input().split()) )
    print( "{:.2f}".format(max(list1) - min(list1)) )
