import numpy as np
import matplotlib.pyplot as plt

# 1. Ask the user how many data points they want
try:
    n = int(input("How many data points do you want to enter? "))
    
    # Initialize empty lists
    x_list = []
    y_list = []

    # 2. Use a for loop to collect each point
    for i in range(n):
        val_x = float(input(f"Enter X value for point {i+1}: "))
        val_y = float(input(f"Enter Y value for point {i+1}: "))
        
        x_list.append(val_x)
        y_list.append(val_y)

    # 3. Convert the lists to NumPy arrays
    x_array = np.array(x_list)
    y_array = np.array(y_list)

    # 4. Perform a NumPy operation (e.g., doubling the Y values)
    # This is where NumPy shines—you can do math on the whole array at once!
    y_modified = y_array * 2 

    # 5. Plot the result
    plt.plot(x_array, y_array, 'o-', label='Original')
    plt.plot(x_array, y_modified, 's--', label='Doubled (NumPy)')
    
    plt.title("NumPy Array Plot")
    plt.legend()
    plt.show()

except ValueError:
    print("Please enter valid numbers!")