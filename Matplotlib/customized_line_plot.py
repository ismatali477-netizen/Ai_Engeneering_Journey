import matplotlib.pyplot as plt
days = [1, 2, 3, 4, 5]
temperature = [28, 30, 29, 31, 32]
plt.plot(days,temperature,color="red",linestyle="--",marker="o",label="Temperature")
plt.title("Temperature")
plt.xlabel("Days")
plt.ylabel("Temperature(°C)")
plt.grid(True)
plt.legend()
plt.show()