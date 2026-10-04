import matplotlib.pyplot as plt

# Data for the linear graph: y = 2x + 1
x = list(range(-5, 6))
y = [2 * value + 1 for value in x]

plt.plot(x, y, marker="o", label="y = 2x + 1")
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Linear Graph: y = 2x + 1")
plt.grid(True)
plt.legend()
plt.show()
