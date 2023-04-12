import matplotlib.pyplot as plt
import numpy as np

# This file is still in development

input_file = open('my_data.txt', 'r')

x = []
y = []
count = 0

for line in input_file.readlines():
    count+=1;
    arr = line.split()
    y.append(float(arr[3]))
    x.append(int(arr[0]))


plt.plot(x, y, label="wpm") # fmt controls the marker and line style
plt.xlabel("Race")
plt.ylabel("WPM")
plt.title("Value vs Date")
plt.grid(True)

coeffs = np.polyfit(x, y, 1)
x2 = np.linspace(0, count) # create 100 points between 0 and 6
y2 = np.polyval(coeffs, x2) # evaluate the polynomial at x2
plt.plot(x2, y2, label="over time")

plt.legend(loc="upper left")

plt.show()
