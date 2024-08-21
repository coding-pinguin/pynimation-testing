import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
from matplotlib.animation import FuncAnimation

# Create the figure and axis
fig, ax = plt.subplots()
fig.set_facecolor('#AFF5BF')

# Set axis limits and aspect ratio
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal', 'box')
ax.axis('off')  # Turn off the axis

# Draw the body of BMO (rectangle)
#body = Rectangle((-1.5, -1.5), 3, 3, color='#58A4B0', ec='black', lw=2)
#ax.add_patch(body)

# Draw the screen (another rectangle inside the body)
#screen = Rectangle((-1, 0), 2, 1.5, color='#A7DDE8', ec='black', lw=2)
#ax.add_patch(screen)

# Draw the eyes (circles inside the screen)
left_eye = Circle((-1, 0.75), radius=0.15, color='black')
right_eye = Circle((1, 0.75), radius=0.15, color='black')
ax.add_patch(left_eye)
ax.add_patch(right_eye)

# Draw the mouth (a simple line initially centered)
mouth = ax.plot([-0.6, 0.6], [0.5, 0.5], color='black', lw=2)[0]

# Animation function to simulate looking left to right and moving the mouth
def animate(frame):
    # Oscillate both the eyes and the mouth along the x-axis
    eye_movement = 0.5 * np.sin(frame * 0.25)  # Oscillate eyes and mouth
    
    # Update eye positions
    new_left_eye_x = -1 + eye_movement
    new_right_eye_x = 1 + eye_movement
    left_eye.center = (0.75, new_right_eye_x)
    right_eye.center = (-0.75, new_right_eye_x)
    
    # Update mouth position by shifting it along the x-axis
    mouth.set_data([-0.6, 0.6], [0.5 + eye_movement, 0.5 + eye_movement])

    return left_eye, right_eye, mouth

# Create the animation
ani = FuncAnimation(fig, animate, frames=np.arange(0, 100), interval=50)

# Show the animation
plt.show()