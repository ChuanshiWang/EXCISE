import random
import math

# Function to calculate distance between two points (player and treasure)
def calculate_distance(pos1, pos2):
    return math.sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)

# Set up the grid and initial parameters
grid_size = 5  # You can modify this size
max_moves = 10  # Set a limit for the number of moves allowed

# Randomly assign positions for player and treasure on the grid
player_position = [random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)]
treasure_position = [random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)]

# Calculate initial distance between player and treasure
initial_distance = calculate_distance(player_position, treasure_position)
moves_made = 0

print("Welcome to the Treasure Hunt!")
print(f"Grid size: {grid_size}x{grid_size}")
print(f"Max moves allowed: {max_moves}\n")

# Main game loop
while moves_made < max_moves:
    print(f"Your current position: {player_position}")
    direction = input("Enter your move (N for North, S for South, E for East, W for West): ").upper()

    # Store the old position to compare distance later
    old_position = player_position.copy()

    # Update player position based on input
    if direction == 'N' and player_position[1] < grid_size - 1:
        player_position[1] += 1
    elif direction == 'S' and player_position[1] > 0:
        player_position[1] -= 1
    elif direction == 'E' and player_position[0] < grid_size - 1:
        player_position[0] += 1
    elif direction == 'W' and player_position[0] > 0:
        player_position[0] -= 1
    else:
        print("Illegal move. Try again.")
        continue

    # Increment moves made
    moves_made += 1

    # Check if the player has found the treasure
    if player_position == treasure_position:
        print("Congratulations! You've found the treasure!")
        break

    # Calculate the new distance after the move
    new_distance = calculate_distance(player_position, treasure_position)

    # Check if the player is getting closer or farther
    if new_distance < initial_distance:
        print("You're getting closer to the treasure.")
    else:
        print("You're moving farther away from the treasure.")

    # Update the initial distance for the next comparison
    initial_distance = new_distance

    # Check if the player has used up all their moves
    if moves_made == max_moves:
        print(f"You've used all {max_moves} moves. Game over!")
        print(f"The treasure was at {treasure_position}.")