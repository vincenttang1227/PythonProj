temp = []
for w in range(4):
    print("Week {:d}:".format(w+1))
    for d in range(3):
        temp.append( eval(input("Day "+str(d+1)+":")) )

print("Average: {:.2f}".format(sum(temp)/len(temp)))
print("Highest:",max(temp))
print("Lowest:",min(temp))
        
