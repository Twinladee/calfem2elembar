import numpy as np
import calfem.core as cfc

Edof = np.array([
    [1, 2, 3, 4],
    [3, 4, 5, 6],
    [7, 8, 3, 4]
])

K = np.matrix(np.zeros((8,8)))
f = np.matrix(np.zeros((8,1)))

E = 1.0e9
A = 0.01

f[3] = 2000

ep = [E,A]

ex1 = np.array([0., 0.])
ex2 = np.array([0., 5.])
ex3 = np.array([0., 0.])

ey1 = np.array([5., 0.])
ey2 = np.array([0., 0.])
ey3 = np.array([-5., 0.])

Ke1 = cfc.bar2e(ex1,ey1,ep)
Ke2 = cfc.bar2e(ex2,ey2,ep)
Ke3 = cfc.bar2e(ex3,ey3,ep)

cfc.assem(Edof[0,:],K,Ke1)
cfc.assem(Edof[1,:],K,Ke2)
cfc.assem(Edof[2,:],K,Ke3)

print("Stiffness matrix K:")
print(K)

bc = np.array([1,2,5,6,7,8])

a, r = cfc.solveq(K,f,bc)

print("Displacements a:")
print(a)

print("Reaction forces r:")
print(r)

ed1 = cfc.extractEldisp(Edof[0,:],a)
N1 = cfc.bar2s(ex1,ey1,ep,ed1)
ed2 = cfc.extractEldisp(Edof[1,:],a)
N2 = cfc.bar2s(ex2,ey2,ep,ed2)
ed3 = cfc.extractEldisp(Edof[2,:],a)
N3 = cfc.bar2s(ex3,ey3,ep,ed3)
print("N1=",N1)
print("N2=",N2)
print("N3=",N3)