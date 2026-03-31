import matplotlib.pyplot as plt
import numpy as np

# Use parentheses () to call the array function
x = np.array([1, 2, 3, 4, 5])
y = np.array([10, 20, 30, 40, 50])

# Use a comma to separate the arguments
plt.plot(x, y)

# Adding labels makes it easier to read
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('My First Plot')

plt.show()