import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,10,50)
y = x**2
print(x)
plt.title('Линейная зависимость x = y') # заголовок
plt.xlabel('x') # ось абсцисс
plt.ylabel('y') # ось ординат
plt.legend # ось ординат
plt.grid() # установить сетку
plt.plot(x,y,'o--')
plt.show()