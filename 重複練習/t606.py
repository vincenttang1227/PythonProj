def compute(rows,cols):
    for i in range(rows):
        for j in range(cols):
            print("{:4d}".format(j-i),end='')
        print()

rows = int( input() )
cols = int( input() )

compute(rows, cols)
