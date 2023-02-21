import matplotlib.pyplot as plt

x_list = []
y_list = []

for x in range(-5, 5):
    y = 5 * x * x + 10 - 30
    x_list.append(x)
    y_list.append(y)

plt.axhline(y = 0, color = 'g')
plt.plot(y_list)
plt.show()