import matplotlib.pyplot as plt

fig = plt.figure()

ax = fig.add_axes([0, 0, 1, 1])
ax.axis('equal')
lang = ['C', 'C++', 'JAVA', 'PYTHON']
stud = ['3', '5', '9', '9']
ax.pie(stud, labels=lang, autopct='%1.2f%%')
plt.show()




