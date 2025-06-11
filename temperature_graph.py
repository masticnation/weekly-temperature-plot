import matplotlib.pyplot as plt

# Data
temps = [20, 22, 19, 23, 21, 24, 20]
days  = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

# Plot
plt.plot(days, temps, marker='o')
plt.title('Temperature Readings Over a Week')
plt.xlabel('Day')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.tight_layout()
plt.show()
