import matplotlib.pyplot as plt
ages = [18, 19, 20, 21, 21, 22, 22, 22, 23, 24, 24, 25, 26, 27, 28]

plt.hist(ages)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()