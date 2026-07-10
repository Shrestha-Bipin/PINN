
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --------------------------------------------------
# Dummy spring-mass data (replace with PINN outputs)
# --------------------------------------------------

t = np.linspace(0, 20, 500)

x1 = 0.8 * np.cos(1.0 * t)
x2 = 0.5 * np.cos(1.0 * t - 0.7)
x3 = 0.3 * np.cos(1.0 * t - 1.4)

# Equilibrium positions
m1_eq = 2.0
m2_eq = 5.0
m3_eq = 8.0

p1 = m1_eq + x1
p2 = m2_eq + x2
p3 = m3_eq + x3

# --------------------------------------------------
# Animation setup
# --------------------------------------------------

fig, ax = plt.subplots(figsize=(10, 3))

ax.set_xlim(-1, 11)
ax.set_ylim(-1, 1)
ax.set_title("Three-Mass Spring System")
ax.set_yticks([])

mass1, = ax.plot([], [], "bo", markersize=15)
mass2, = ax.plot([], [], "ro", markersize=15)
mass3, = ax.plot([], [], "go", markersize=15)

spring1, = ax.plot([], [], "k-")
spring2, = ax.plot([], [], "k-")
spring3, = ax.plot([], [], "k-")
spring4, = ax.plot([], [], "k-")


def spring_shape(x_start, x_end, coils=12, amp=0.08):
    xs = np.linspace(x_start, x_end, coils)
    ys = np.zeros(coils)
    ys[1:-1:2] = amp
    ys[2:-1:2] = -amp
    return xs, ys


def update(frame):
    xm1 = p1[frame]
    xm2 = p2[frame]
    xm3 = p3[frame]

    mass1.set_data([xm1], [0])
    mass2.set_data([xm2], [0])
    mass3.set_data([xm3], [0])

    xs, ys = spring_shape(0, xm1)
    spring1.set_data(xs, ys)

    xs, ys = spring_shape(xm1, xm2)
    spring2.set_data(xs, ys)

    xs, ys = spring_shape(xm2, xm3)
    spring3.set_data(xs, ys)

    xs, ys = spring_shape(xm3, 10)
    spring4.set_data(xs, ys)

    return (
        mass1, mass2, mass3,
        spring1, spring2, spring3, spring4
    )


ani = FuncAnimation(
    fig,
    update,
    frames=len(t),
    interval=20,
    blit=True
)

plt.show()

# Optional:
ani.save("spring_mass.gif", writer="pillow", fps=30)
ani.save("spring_mass.mp4", writer="ffmpeg", fps=30)
