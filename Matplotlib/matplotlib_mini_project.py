import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
study_hours = [2, 4, 3, 5, 6]

subjects = ["Math", "Science", "English", "Computer"]
marks = [88, 92, 81, 95]

ages = [18, 19, 20, 21, 21, 22, 22, 22, 23, 24, 24, 25, 26]

sleep = [5, 6, 7, 8, 9]
productivity = [55, 65, 75, 82, 90]

expenses = ["Food", "Transport", "Books", "Entertainment"]
amount = [300, 150, 200, 100]
plt.plot(days,study_hours,color="blue",marker="o",label="Study Hours")
plt.title("Daily Study Hours")
plt.xlabel("Days")
plt.ylabel("Hours")
plt.grid(True)
plt.legend()
plt.show()
plt.bar(subjects,marks)
plt.title("Subject Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()
plt.hist(ages)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()
plt.scatter(sleep,productivity)
plt.title("Sleep vs Productivity")
plt.xlabel("Hours of Sleep")
plt.ylabel("Productivity")
plt.show()
plt.pie(amount,labels=expenses)
plt.title("Monthly Expenses")
plt.show()
