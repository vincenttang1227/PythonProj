set1 = set('abcdefghijklmnopqrstuvwxyz')

times = int( input() )
for i in range(times):
    set2 = set( input().lower() )
    print( set2>=set1 )
