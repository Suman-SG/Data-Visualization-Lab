import numpy as np
import matplotlib.pyplot as plt

# 1. Ask the user how many data points they want
try:
    n = int(input("How many data points do you want to enter? "))
    
    # Initialize empty lists
    x_list = []
    

    # 2. Use a for loop to collect each point
    for i in range(n):
        val_x = float(input(f"Enter X value for point {i+1}: "))
        
        x_list.append(val_x)
       

    # 3. Convert the lists to NumPy arrays
    x_array = np.array(x_list)
    

    # 4. Perform a NumPy operation (e.g., doubling the Y values)
    
    
    plt.hist(x_array)
    plt.show()

except ValueError:
    print("Please enter valid numbers!")