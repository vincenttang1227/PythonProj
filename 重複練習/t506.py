def compute(a, b, c):
    d = b**2 - 4*a*c
    if d >= 0:
        ans1 = (-b + d**0.5)/(2*a)
        ans2 = (-b - d**0.5)/(2*a)
        return ans1, ans2
    else:
        return "Your equation has no root.", ""

a = int( input() )
b = int( input() )
c = int( input() )
a1, a2 = compute(a,b,c)
if str(a2) == "":
    print(a1)
else:
    print(a1,", ",a2,sep="")
