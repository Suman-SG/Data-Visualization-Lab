import matplotlib.pyplot as plt

try:
    # 1. Ask for number of slices
    n = int(input("How many slices do you want in your pie chart? "))
    
    labels = []
    sizes = []

    # 2. Collect user input
    for i in range(n):
        label = input(f"Enter label for slice {i+1}: ")
        size = float(input(f"Enter value for '{label}': "))
        
        labels.append(label)
        sizes.append(size)

    # 3. Plotting the result
    plt.figure(figsize=(7, 7))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title("Dynamic User-Generated Pie Chart")
    plt.axis('equal') 
    plt.show()

except ValueError:
    print("Error: Please enter numbers for the count and values.")