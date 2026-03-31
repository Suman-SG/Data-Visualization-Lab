import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Generate random dataset
np.random.seed(42)

data = {
    "radius_mean": np.random.uniform(10, 30, 30),
    "perimeter_mean": np.random.uniform(50, 150, 30)
}

df = pd.DataFrame(data)

# Select features
x = df['radius_mean']
y = df['perimeter_mean']

# Create clusters
x1, y1 = x[:15], y[:15]
x2, y2 = x[15:], y[15:]

# Add outliers
x_out = [x.mean() + 10, x.mean() - 5]
y_out = [y.mean() + 50, y.mean() - 50]

# --- Create subplot ---
plt.figure(figsize=(10, 5))

# 🔹 Scatter Plot
plt.subplot(1, 2, 1)
plt.scatter(x1, y1, label="Cluster 1")
plt.scatter(x2, y2, label="Cluster 2")
plt.scatter(x_out, y_out, label="Outliers")
plt.title("Scatter Plot")
plt.xlabel("Radius Mean")
plt.ylabel("Perimeter Mean")
plt.legend()

# 🔹 Bar Graph
plt.subplot(1, 2, 2)
means = [x.mean(), y.mean()]
labels = ["Radius Mean", "Perimeter Mean"]

plt.bar(labels, means)
plt.title("Bar Graph (Means)")

# Show both plots
plt.tight_layout()
plt.show()