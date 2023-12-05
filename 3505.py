x = int(input())
y = int(input())
z = int(input())
if x >= y >= z:
    print(x)
elif x >= z >= y:
    print(x)
elif y >= x >= z:
    print(y)
elif y >= z >= x:
    print(y)
else:
    print(z)