# Function to display the room
import random


def display(room):
    print(room)

# Initialize the room as a 4x4 grid, all elements set to 1 (dirty)
room = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
]
print("All the rooms are dirty")
display(room)

# Randomly dirty some rooms
x = 0  # Initialize the row index
y = 0  # Initialize the column index
