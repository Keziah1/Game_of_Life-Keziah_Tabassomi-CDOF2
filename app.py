import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the size of the grid
grid_size = (50, 50)

# Create a random initial state for the grid
initial_state = np.random.choice([0, 1], size=grid_size, p=[0.5, 0.5])

# Define the rules of the game
def update_state(state):
    neighbors_count = sum(np.roll(np.roll(state, i, 0), j, 1)
                          for i in (-1, 0, 1) for j in (-1, 0, 1)
                          if (i != 0 or j != 0))
    new_state = (neighbors_count == 3) | (state & (neighbors_count == 2))
    return new_state

# Create a figure and axis for the animation
fig, ax = plt.subplots()

# Create an image plot for the grid
img = ax.imshow(initial_state, cmap='binary')

# Function to update the grid state for each animation frame
def update(frame):
    img.set_array(update_state(img.get_array()))
    return img,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=200, blit=True)

# Show the animation
plt.show()
