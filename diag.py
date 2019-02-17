import Kitaev as ktv
import numpy as np

N = 3
Hamil = ktv.get_Hamil(N)
# print(Hamil)

import numpy.linalg as linalg
w,v = linalg.eigh(Hamil)

#    print w, v
#    print '\n\n'
"""
    
    U = np.zeros([2*N**2,2*N**2])
    D = np.zeros([2*N**2,2*N**2])
    for i in range(len(w)):
        D[i,i] = w[i]
        for j in range(len(w)):
            U[i,j] = v[i,j]
    
    H = np.matmul(D, U.transpose())
    H = np.matmul(U, H)
    #print H - Hamil
    print np.matmul(H,U) - np.matmul(U,D)
"""


def occup():
    pass











