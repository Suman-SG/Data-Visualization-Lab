import matplotlib.pyplot as plt

# Fixed data
labels = ['Python', 'Java', 'C++', 'JavaScript']
sizes = [45, 25, 15, 15]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

# Plotting the pie chart
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title("Static Pie Chart: Programming Popularity")
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()