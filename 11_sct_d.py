import matplotlib.pyplot as plt

try:
    # 1. Ask how many points to plot
    n = int(input("How many points do you want to plot? "))
    
    x_coords = []
    y_coords = []

    # 2. Collect coordinates
    for i in range(n):
        print(f"\nPoint {i+1}:")
        x = float(input(f"  Enter X value: "))
        y = float(input(f"  Enter Y value: "))
        
        x_coords.append(x)
        y_coords.append(y)

    # 3. Create the plot
    plt.figure(figsize=(8, 5))
    plt.scatter(x_coords, y_coords, c='blue', s=100, edgecolors='black', alpha=0.7)

    # 4. Add styling
    plt.title("Dynamic User-Generated Scatter Plot", fontsize=14)
    plt.xlabel("X-Axis Values")
    plt.ylabel("Y-Axis Values")
    plt.axhline(0, color='black', linewidth=1) # Adds a horizontal line at 0
    plt.axvline(0, color='black', linewidth=1) # Adds a vertical line at 0
    plt.grid(True)

    plt.show()

except ValueError:
    print("Invalid input! Please enter numbers only.")