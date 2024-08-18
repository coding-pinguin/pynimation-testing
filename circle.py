import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set up the figure, axis, and plot element to animate
fig, ax = plt.subplots()
ax.set_aspect('equal', 'box')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

# Create a circle object
circle1, = ax.plot([], [], 'ko', markersize=15)  # 'bo' means blue circle marker
circle2, = ax.plot([], [], 'ko', markersize=15)
# Parameters for the circular motion
radius = 1  # Radius of the circular path
omega = 2 * np.pi / 100  # Angular velocity in radians per frame

# Initialization function for the animation
def init():
    circle1.set_data([], [])
    circle2.set_data([], [])
    return circle1, circle2,

# Animation function that updates the circle's position
def animate(frame):
    # Calculate the new position of the circle
    x = radius * np.cos(omega * frame)
    y = radius * np.sin(omega * frame)
    
    # Update the circle's position
    circle1.set_data([x], [y])
    circle2.set_data([-x],[-y])
    return circle1, circle2,

# Create the animation
animation = FuncAnimation(fig, animate, frames=range(200), init_func=init, blit=True, interval=50)

# Show the animation
plt.show()