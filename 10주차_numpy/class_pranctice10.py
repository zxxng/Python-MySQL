import numpy as np

실습1
array_a = np.array([0,1,2,3,4,5,6,7,8,9])
array_b = np.array(range(0,10))
array_c = np.array(range(0,10,2))

print("실습 1: array_a = ", array_a)
print("실습 2: array_b = ", array_b)
print("실습 3: array_c = ", array_c)
print("array_c의 shape : ", array_c.shape)
print("array_c의 ndim : ", array_c.ndim)
print("array_c의 dtype : ", array_c.dtype)
print("array_c의 size : ", array_c.size)
print("array_c의 itemsize : ", array_c.itemsize)


실습2
heights = np.array([1.83, 1.76, 1.69, 1.86, 1.77, 1.73])
weights = np.array([86, 74, 59, 95, 80, 68])

BMI = weights / heights**2

print("대상자들의 키 : ", heights)
print("대상자들의 몸무게 : ", weights)
print("대상자들의 BMI : ", BMI)

# 실습3
x = np.array([['a','b','c','d'],['c','c','g','h']])
print(x[x =='c'])
mat_a = np.array([[10,20,30],[10,20,30]])
mat_b = np.array([[2,2,2],[1,2,3]])
print(mat_a + mat_b)

실습4
x = np.array([[1.83, 1.76, 1.69, 1.86, 1.77, 1.73],
                [86.0, 74.0, 59.0, 95.0, 80.0, 68.0]])
y = x[0:2, 1:3]
z = x[0:2]


print("x shape : ", x.shape)
print("y shape : ", y.shape)
print("z shape : ", z.shape)
print("y valuse = : ", y)
print("z valuse = : ", z)

BMI = x[1] / x[0]**2
print("BMI data ", BMI)

실습5
player = [[170, 76.4], [183, 86.2], [181, 78.5], [176, 80.1]]

np_array = np.array(player)

print("몸무게가 80 이상인 선수 정보\n", np_array[np_array[:,1] >= 80])
print("키가 180 이상인 선수 정보\n", np_array[np_array[:,0] >= 180])


