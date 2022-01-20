'''joining numpy arrays'''
import numpy as np
n1=np.array([10,0,30])
n2=np.array([40,50,60])
np.vstack((n1,n2))

#output
# array([[10,  0, 30],
#        [40, 50, 60]])

n1=np.array([10,0,30])
n2=np.array([40,50,60])
np.hstack((n1,n2))

# output
# array([10,  0, 30, 40, 50, 60])

n1=np.array([10,0,30])
n2=np.array([40,50,60])
np.column_stack((n1,n2))

# array([[10, 40],
#        [ 0, 50],
#        [30, 60]])
