'''Addition of Numpy Arrays'''

import numpy as np
n1=np.array([10,20])
n2=np.array([30,40])

np.sum([n1,n2])

# 100

np.sum([n1,n2],axis=0)
# array([40, 60])

np.sum([n1,n2],axis=1)
# array([30, 70])
