import numpy as np
import time
myArray = np.array(2) #0-D
print(myArray)
array1D = np.array([[1,2,3],[4,5,6]])
array1D2 = np.array([[1,2,3],[4,5,6]])
startTime = time.time()
sumNumpy = array1D+array1D2
endTime = time.time() - startTime
print("numpy sum: ", endTime)
print(array1D.shape)
startTime = time.time()
for i in range(array1D.shape[0]):
    for j in range(array1D.shape[1]):
        print(array1D[i,j]+array1D2[i,j])
endTime = time.time() - startTime
print("manual sum: ", endTime)