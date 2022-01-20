'''Numpy Intersection and Difference'''

import numpy as np
n1=np.array([10,20,30,40,50,60])
n2=np.array([50,60,70,80,90])
np.intersect1d(n1,n2)

# array([50, 60])

np.setdiff1d(n1,n2)
# array([10, 20, 30, 40])

np.setdiff1d(n2,n1)
# array([70, 80, 90])
