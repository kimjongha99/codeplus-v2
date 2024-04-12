def descending_grid(n):
    grid = []
    for i in range(n):
        row = list(range(n, 0, -1))  # Create a row with descending values from n to 1
        grid.append(row)
    return grid

# Example with N=3
n = int(input())
grid = descending_grid(n)


for row in grid:
    print(' '.join(map(str, row)))
