import numpy as np

a0 = np.loadtxt('a1.txt')
a1 = a0.astype(int)
n = a1.shape[0]
c1 = a1
print(a1[0],a1[1],a1[2])
e1=[];
e1.append(a1[0])
for i in range(1,n):
    d1 = a1[i]-a1[i-1]
    e1.append(d1)

print(e1)
f1 = np.asarray(e1)
f1=f1.astype(int)
print(f1)

np.savetxt('b1.txt',f1,fmt = "%d")

