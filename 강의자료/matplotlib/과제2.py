import matplotlib.pyplot as plt

dac_length = [77,78,85,83,73,77,73,80]
dac_height = [25,28,29,30,21,22,17,35]
samo_length = [75,77,86,86,79,83,83,88]
samo_height = [56,57,50,53,60,53,49,61]
mal_length = [34,38,38,41,30,37,41,35]
mal_height = [22,25,19,30,21,24,28,18]

plt.scatter(dac_length, dac_height, color='red')
plt.scatter(samo_length, samo_height, color='blue', marker = 's')
plt.scatter(mal_length, mal_height, color='green', marker='^')

plt.legend(('Dachshund','Samoyed','Maltese'),loc='upper left')

plt.title("Dog size")
plt.xlabel("Length")
plt.ylabel("Hight")

plt.show()