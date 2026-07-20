import matplotlib.pyplot as plt
expenses = ["Food", "Transport", "Books", "Entertainment"]
amount = [300, 150, 200, 100]
plt.pie(amount,labels=expenses)
plt.title("Monthly Expenses")
plt.show()