# Island Perimeter

## Description

This project involves calculating the perimeter of an island in a grid. The grid is represented by a 2D list of integers where:
- `0` represents water.
- `1` represents land.

The island is a contiguous group of land cells, and the perimeter is defined by the boundary of the island that is adjacent to water or the grid's boundary.

The task is to implement a function that calculates and returns the perimeter of the island.

## Problem Statement

You are given a grid that is completely surrounded by water, and there is only one island or no island at all. The island doesn't have "lakes" (water inside that isn't connected to the surrounding water). The grid is a rectangular matrix where each cell is a square of side length 1. Cells are connected horizontally and vertically, but not diagonally.

### Function Signature
```python
def island_perimeter(grid: List[List[int]]) -> int:
```

### Input:
- `grid`: A 2D list where:
  - `1` represents land.
  - `0` represents water.
  - The grid has at most dimensions of 100x100.

### Output:
- The function should return an integer representing the perimeter of the island.

### Example:

Given the following grid:

```python
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
```

The expected output is:
```
12
```

## Solution

### Approach

1. **Iterate over each cell** in the grid.
2. If the cell is land (`1`), check its four adjacent cells (up, down, left, and right).
3. If any adjacent cell is water (`0`) or out of bounds, that side contributes to the perimeter.
4. Sum all the perimeter contributions from each land cell to calculate the total perimeter.

### Algorithm:
1. Loop through each cell in the grid.
2. For each land cell, check its four neighbors:
   - If any of the neighbors is water (`0`) or out of bounds, count that side as part of the perimeter.
3. Return the total perimeter.

### Code Implementation:
```python
#!/usr/bin/python3
"""
Function that calculates the perimeter of the island described in the grid.
"""

def island_perimeter(grid):
    """
    Calculate the perimeter of an island in a grid.
    
    Args:
    grid (list of list of int): 2D list representing the grid where:
                                - 0 represents water
                                - 1 represents land
    
    Returns:
    int: the perimeter of the island
    """
    perimeter = 0
    
    # Get the number of rows and columns in the grid
    rows = len(grid)
    cols = len(grid[0])

    # Iterate over each cell in the grid
    for i in range(rows):
        for j in range(cols):
            # If the current cell is land (1)
            if grid[i][j] == 1:
                # Check each of the 4 adjacent sides (up, down, left, right)
                # Top side (up): If it's out of bounds or water, it's part of the perimeter
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                # Bottom side (down): If it's out of bounds or water, it's part of the perimeter
                if i == rows - 1 or grid[i+1][j] == 0:
                    perimeter += 1
                # Left side (left): If it's out of bounds or water, it's part of the perimeter
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                # Right side (right): If it's out of bounds or water, it's part of the perimeter
                if j == cols - 1 or grid[i][j+1] == 0:
                    perimeter += 1

    return perimeter
```

## Requirements

- **Python version**: The solution is written in Python 3.4.3.
- **Libraries**: No external libraries are required.
- **Code Style**: The code follows the PEP 8 style guide.

## Execution

1. Clone the repository.
2. Navigate to the directory `0x09-island_perimeter`.
3. Run the script:
   ```bash
   ./0-main.py
   ```

### Example Execution:
For the given example grid, running the script will produce:
```
12
```

## Edge Cases

1. **Empty Grid**: If the grid contains no land cells (`1`), the perimeter will be `0`.
2. **Smallest Grid**: A grid with only one land cell like `[[1]]` will return a perimeter of `4`.
3. **Grid with Boundary Water**: The grid is surrounded by water, so checking the edges is unnecessary, but we must account for boundary conditions.

## Time Complexity

- The time complexity of this solution is \(O(n \times m)\), where \(n\) and \(m\) are the number of rows and columns in the grid. We iterate through each cell once and perform constant-time checks for its neighbors.

## Author

This solution was created as part of the **0x09-Island Perimeter** project at **ALX**.
