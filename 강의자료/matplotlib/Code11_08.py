import matplotlib.pyplot as plt

books = [1,6,2,3,1,2,0,2]

plt.hist(books, bins = 6)

plt.xlabel("books")
plt.ylabel("frequency")
plt.show()