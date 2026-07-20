import matplotlib.pyplot as plt
hours_sleep = [5, 6, 7, 8, 9, 10]
productivity = [50, 60, 70, 80, 85, 90]
plt.scatter(hours_sleep,productivity)
plt.title("Sleep vs Productivity")
plt.xlabel("Hours of Sleep")
plt.ylabel("Productivity")
plt.show()