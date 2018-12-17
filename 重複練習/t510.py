def fib( n ):
    if n < 2:
        return n
    else:
        return fib(n-1)+fib(n-2)

def compute(num):
    for i in range(num):
        print( fib(i), end=' ')

compute( int(input()) )
