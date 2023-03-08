import numpy as np

players = np.array([[170, 76.4], [183, 86.2], [181, 78.5], [176, 80.1]])

print('몸무게가 80 이상인 선수 정보 : ', players[players[:, 1]>=80.0])
print('키가 180 이상인 선수 정보 : ', players[players[:, 0]>=180.0])
