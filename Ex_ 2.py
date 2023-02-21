import numpy as np
import matplotlib.pyplot as plt

size = 15
houses = np.random.randint(100, 300, size)
prices = np.random.randint(3000000, 20000000, size)
avg_prices = [round(prices[i]/houses[i]) for i in range(len(prices))]
print(f'Стоимость квадратного метра домов: {avg_prices}')

sorted = []
for i in range(len(avg_prices)):
    if (avg_prices[i] < 50000):
        sorted.append(avg_prices[i])

sorted.sort()
print(f'Подходящие дома: {sorted}')        

plt.axhline(y = 50000, color = 'g', linestyle = '--')
plt.plot(avg_prices, 'ro')

plt.show()
