from matplotlib import pyplot

#1. prepare data
machine_types = [18, 4, 2]

#2. prepare label
machine_names =["PC", "Mac", "Linux"]

#3. draw pie
pyplot.pie(machine_types, labels=machine_names, autopct="%.1f%%", shadow=True, explode=[0, 0.2, 0])
pyplot.title("Users' type")
pyplot.axis("equal")
#4. show
pyplot.show()