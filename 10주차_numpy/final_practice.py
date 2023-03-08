import numpy as np

# np_array = np.array([[1,2,3],[4,5,6],[7,8,9]])

# print(np_array[np_array[:,2] > 5])

# print(np.logspace(5,10,num=10))


# np_array = np.array([1,2,3,4,5,6])
# new_array = np_array.reshape(2,3)
# print(new_array)
# new2_array = new_array.flatten()
# print(new2_array)

rand_array = np.random.seed(100)
print(rand_array)
print(np.random.rand(5,3))
print(np.random.randint(1, 7, size=(4,7)))

np_array = np.random.randint(3,10, size=5)
print(np_array)
print(np.mean(np_array))
print(np.median(np_array))