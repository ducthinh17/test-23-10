import numpy as np


data_1 = (5, 2.5, 3.5, 1.5, 4,2, 5, 5, 4,3, 3.5, 4, 4,3, 3.5, 5, 2,5,2)
mean = np.mean(data_1)
std= np.std(data_1)

z = (3- mean)/std
print('mean: ',mean)
print('sd: ',std)
s=sum(data_1)
per= ()
print(z)