a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = " "
for i in range(c, d+1):
    e += "\t" + str(i)

print(e)

for j in range(a, b+1):
    e = str(j)
    for i in range(c, d+1):
        e += "\t" + str(i * j)
    print(e)

