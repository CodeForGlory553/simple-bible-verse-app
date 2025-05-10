
import numpy as np

# initialize the grid with random values
rows, cols = 10, 10
grid = np.random.randint(0, 2, size=(rows, cols))
print("Initial grid:\n", grid)  # Corrected printing of initial grid

# update the grid based on the rules of the game
def count_live_neighbours(grid, row, col):
    rows, cols = grid.shape
    live_neighbours = 0
    for i in range(max(0, row - 1), min(rows, row + 2)):
        for j in range(max(0, col - 1), min(cols, col + 2)):
            if (i == row and j == col):  # Changed the condition here
                continue
            live_neighbours += 1
    return live_neighbours



def next_generation(grid):
    rows, cols = grid.shape
    new_grid = np.zeros((rows, cols), dtype=int)
    for i in range(rows):
        for j in range(cols):
            live_neighbours = count_live_neighbours(grid, i, j)
            if grid[i][j] == 1 and (live_neighbours < 2 or live_neighbours > 3):
                new_grid[i][j] = 0
            elif grid[i][j] == 0 and live_neighbours == 3:
                new_grid[i][j] = 1
            else:
                new_grid[i][j] = grid[i][j]
    return new_grid


# run the simulation for a number of generations
num_generations = 5
for gen in range(num_generations):
    print(f"Generation {gen + 1}:\n")  # Added newline for better formatting
    grid = next_generation(grid)
    print(f"{grid}\n") #changed "Final Grid" to just the grid
