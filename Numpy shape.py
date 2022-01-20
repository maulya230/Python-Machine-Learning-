'''checking shape of Numpy arrays'''
import numpy as np
n1=np.array([[1,2,3],[4,5,6]])
n1.shape

# output
# (2,3)

n1.shape=(3,2)
n1
#output
# array([[1, 2],
#        [3, 4],
#        [5, 6]])
