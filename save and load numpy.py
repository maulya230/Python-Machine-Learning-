import numpy as np
n1=np.array([10,20,30,40,50,60])
np.save('my_numpy',n1)
n2=np.load("my_numpy.npy")
n2

# array([10, 20, 30, 40, 50, 60])
