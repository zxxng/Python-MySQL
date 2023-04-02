import matplotlib.pyplot as plt

month = [7,8,9,10,11,12] # x축 = [x for in range(7,13)]
new_user = [456, 492, 578, 599, 670, 854] # y축
 
fig, axs = plt.subplots(1, 4, figsize=(10, 3))

axs[0].bar(month, new_user)
axs[1].plot(month, new_user)
axs[2].scatter(month, new_user)
axs[3].barh(month, new_user)
         
plt.title("Daehan company speeda net new Costomers") # 제목 설정
plt.ylabel("user") # y축 레이블 입력
plt.xlabel("month")
plt.show()


