##sum of all increasing subsecuences of length 4 where a[i]=num^i (mod prim)
# and i_max=n
# time and memory nlogn
n=10000
b=1
prim = 10000019
num=151
d = dict()
num_big = list()
a=list()
for i in range (1,n+1):

    b = num*b % prim
    a.append(b)
    
sorted_arr = sorted(a)
for i in range (1,n+1):
    d[sorted_arr[i-1]]=i

for i in range (1,n+1):
    num_big.append(   [a[i-1],d[a[i-1]],i]   )

perm = list()
for el in num_big:
    perm.append(el[1])
#print (perm)

###########
dp = [[0] * (n + 1) for i in range(6)]

def query(row, i):
    r = 0
    while i > 0:
        r += row[i]
        i -= i & -i
    return r
 
def update(row, i, r):
    while i <= n:
        row[i] += r
        i += i & -i
 
res = [[1] * n for i in range(6)]
for i in range(n):
    update(dp[0], perm[i], 1)
    
    res[0][i] = query(dp[0], perm[i] - 1)
    update(dp[1], perm[i], res[0][i])
    
    res[1][i] = query(dp[1], perm[i] - 1)
    update(dp[2], perm[i], res[1][i])

    res[2][i] = query(dp[2], perm[i] - 1)
#    update(dp[3], a[i], res[2][i])   


perm = perm[::-1]

for i in range(n):
    perm[i] = n+1-perm[i]
#print(sum(res))
####
for i in range(n):
    update(dp[3], perm[i], 1)
    
    res[3][i] = query(dp[3], perm[i] - 1)
    update(dp[4], perm[i], res[3][i])
    
    res[4][i] = query(dp[4], perm[i] - 1)
    update(dp[5], perm[i], res[4][i])

    res[5][i] = query(dp[5], perm[i] - 1)
####
#print (res[0])
#print (res[1])
#print (res[2])
res[3] = res[3][::-1]
res[4] = res[4][::-1]
res[5] = res[5][::-1]
#print (res[3])
#print (res[4])
#print (res[5])
rez = list()
for i in range(n):
    rez.append(res[0][i]*res[4][i]+res[1][i]*res[3][i]+res[5][i]+res[2][i])
#print (rez)
s=0
for i in range(n):
    s+=((a[i]*rez[i]))#%1000000007)
#s%=1000000007
print (s)