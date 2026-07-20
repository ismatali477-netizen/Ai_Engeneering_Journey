import matplotlib.pyplot as plt
subjects = ["Math", "Science", "English", "Computer"]
marks = [88, 92, 81, 95]

plt.bar(subjects,marks)
plt.title("Subject Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()