import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

theta = [-5, 0, 5, 10]
voltage = [-0.85, -0.014, 0.844, 1.7]
print(linregress(theta, voltage))
plt.plot(theta, voltage, color='green', linestyle='dashed', linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=8)
plt.xlabel('Theta - axis')
plt.ylabel('Voltage - axis')
plt.title('Ratio angle-voltage')
plt.savefig("Ratio angle-voltage")

