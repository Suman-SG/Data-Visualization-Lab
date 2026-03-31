import matplotlib.pyplot as plt

# Fixed data points
x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

plt.scatter(x, y, color='hotpink', marker='o')

plt.title("Static Scatter Plot: Car Age vs Speed")
plt.xlabel("Age of Car (Years)")
plt.ylabel("Top Speed (mph)")
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()