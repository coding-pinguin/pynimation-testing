import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle, Arc

# Create the figure and axis
fig, ax = plt.subplots()

# Set axis limits and aspect ratio
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal', 'box')
ax.axis('off')  # Turn off the axis

# Draw the face (circle)
face = Circle((0, 0), radius=1.5, color='yellow', ec='black')
ax.add_patch(face)

# Draw the eyes
left_eye = Circle((-0.6, 0.5), radius=0.2, color='white', ec='black')
right_eye = Circle((0.6, 0.5), radius=0.2, color='white', ec='black')
ax.add_patch(left_eye)
ax.add_patch(right_eye)

# Draw the pupils
left_pupil = Circle((-0.6, 0.5), radius=0.1, color='black')
right_pupil = Circle((0.6, 0.5), radius=0.1, color='black')
ax.add_patch(left_pupil)
ax.add_patch(right_pupil)

# Create the initial mouth as a straight line (arc with no curvature)
mouth = Arc((0, -0.7), width=1.0, height=-0.1, angle=0, theta1=0, theta2=180, color='black', lw=2)
ax.add_patch(mouth)

# Animation function to transition from straight face to a smile
def animate(frame):
    # Calculate the new mouth curvature for the smile transition
    new_height = -0.4 * ( (frame+1) / 100)  # Smooth transition to curved smile
    mouth.set_height(new_height)  # Update the height of the mouth
    return mouth,

# Create the animation
ani = FuncAnimation(fig, animate, frames=200, interval=50, blit=False)

# Show the animation
plt.show()