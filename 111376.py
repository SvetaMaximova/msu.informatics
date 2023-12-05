v = [[0]] * 8
for i in range(0, 8):
    v[i] = v[i] * 8
for i in range(0, 8):
    for j in range(0, 8):
        v[i][j] = '.'
        
where = input()
k = 0
m = int(where[1])
if where[0] == 'a':
    k = 0
elif where[0] == 'b':
    k = 1
elif where[0] == 'c':
    k = 2
elif where[0] == 'd':
    k = 3
elif where[0] == 'e':
    k = 4
elif where[0] == 'f':
    k = 5
elif where[0] == 'g':
    k = 6
elif where[0] == 'h':
    k = 7
v[8 - m][k] = 'K'

if (m <= 6) and (k >= 1):
    v[8 - m - 2][k - 1] = '*'
if (m <= 6) and (k <= 6):
    v[8 - m - 2][k + 1] = '*'
    
if (m >= 3) and (k >= 1):
    v[8 - m + 2][k - 1] = '*'
if (m >= 3) and (k <= 6):
    v[8 - m + 2][k + 1] = '*'
        
if 1 <= m < 8 and k >= 2:
    v[8 - m - 1][k - 2] = '*'
if 1 <= m < 8 and k <= 5:
    v[8 - m - 1][k + 2] = '*'
 
    
if 1 < m <= 8 and k >= 2:
    v[8 - m + 1][k - 2] = '*' 
if 1 < m <= 8 and k <= 5:
    v[8 - m + 1][k + 2] = '*'
    
for i in range(0, 8):
    for j in range(0, 8):
        if j != 0:
            print(f' {v[i][j]}', end = '')
        else:
            print(f'{v[i][j]}', end = '')
    print()