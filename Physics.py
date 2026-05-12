import numpy as np
import matplotlib.pyplot as plt

angle = float(input("Угол (градусы): "))
mu = float(input("Коэффициент трения: "))
g = 9.81
a = g * (np.sin(np.radians(angle)) - mu * np.cos(np.radians(angle)))
if a < 0: a = 0

dt = 0.1
t = np.arange(0, 10, dt)
v = np.zeros(len(t))
acc = np.full(len(t), a)

for i in range(1, len(t)):
    v[i] = v[i-1] + a * dt

fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.plot(t, v)
ax2.plot(t, acc, color='r')
ax1.set_ylabel('Скорость (м/с)')
ax2.set_ylabel('Ускорение (м/с^2)')
ax2.set_xlabel('Время (с)')
plt.show()