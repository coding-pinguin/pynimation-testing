import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Ellipse
from matplotlib.animation import FuncAnimation

# Create the figure and axis
fig, ax = plt.subplots()

# Set axis limits and aspect ratio
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal', 'box')
ax.axis('off')  # Turn off the axis

# Draw the face (circle)
#face = Circle((0, 0), radius=1.5, color='yellow', ec='black')
#ax.add_patch(face)

# Draw the eyes
left_eye = Circle((-0.6, 0.5), radius=0.2, color='black', ec='black')
right_eye = Circle((0.6, 0.5), radius=0.2, color='black', ec='black')
ax.add_patch(left_eye)
ax.add_patch(right_eye)

# Draw the pupils
#left_pupil = Circle((-0.6, 0.5), radius=0.1, color='black')
#right_pupil = Circle((0.6, 0.5), radius=0.1, color='black')
#ax.add_patch(left_pupil)
#ax.add_patch(right_pupil)

# Create the mouth as an Ellipse
mouth = Ellipse((0, -0.5), width=1.0, height=0.2, color='black')
ax.add_patch(mouth)

# Animation function to simulate talking by changing the mouth size
def animate(frame):
    # Change the mouth height to simulate talking
    height = 0.2 + 0.1 * np.sin(frame * 0.2)  # Mouth opens and closes
    mouth.set_height(height)
    return mouth,

# Create the animation
ani = FuncAnimation(fig, animate, frames=np.arange(0, 100), interval=100, blit=True)

# Show the animation
plt.show()