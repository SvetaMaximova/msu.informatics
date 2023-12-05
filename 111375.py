n = int(input())
v = [[1]] * n
for i in range(0, n):
    v[i] = v[i] * (i+1)
    
for i in range(2, n):
    for j in range(1, i):
        v[i][j] = v[i - 1][j - 1] + v[i - 1][j]
    
for i in range(0, n): 
    for j in range(0, i+1):
        print(str(v[i][j]).rjust(6), end='')
    if i != n - 1:
        print()
