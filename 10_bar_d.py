import numpy as np
import matplotlib.pyplot as plt

try:
    # 1. Ask for the number of categories
    n = int(input("How many categories (bars) do you want? "))
    
    labels = []
    values = []

    # 2. Collect labels and values
    for i in range(n):
        label = input(f"Enter label for bar {i+1} (e.g., Category Name): ")
        val = float(input(f"Enter value for '{label}': "))
        
        labels.append(label)
        values.append(val)

    # 3. Convert to NumPy array for easy manipulation
    y_values = np.array(values)

    # 4. Plotting the Bar Chart
    plt.figure(figsize=(8, 6))
    
    # Using plt.bar for the bar chart
    bars = plt.bar(labels, y_values, color='skyblue', edgecolor='navy')

    # Optional: Add a title and labels
    plt.title("User-Generated Data Chart", fontsize=14)
    plt.xlabel("Categories")
    plt.ylabel("Values")

    # Show the plot
    plt.show()

except ValueError:
    print("Oops! Please make sure to enter numbers for the values.")