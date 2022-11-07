import matplotlib.pyplot as plt
#import numpy as np

year = [1972, 1982, 1992, 2002, 2012]
e_india = [100.6, 158.61, 305.54, 394.96, 724.79]
e_bangladesh = [10.5, 25.21, 58.65, 119.27, 274.87]

plt.plot(year, e_india, color="orange", label="India")
plt.plot(year, e_bangladesh, color="g", label="Bangladesh")

plt.xlabel('Years')
plt.ylabel('Power')
plt.title("Comparison")
plt.legend()

plt.show()
