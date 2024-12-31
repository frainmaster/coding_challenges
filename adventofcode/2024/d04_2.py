with open('d04.txt') as f:
    grid = f.readlines()


ans = 0


for row_idx, row in enumerate(grid[1:-1]):
    r = row_idx + 1
    for col_idx, char in enumerate(row[1:-1]):
        c = col_idx + 1
        if char != "A":
            continue
        if grid[r-1][c-1] == grid[r-1][c+1] == "M" and grid[r+1][c+1] == grid[r+1][c-1] == "S":
            ans += 1
        elif grid[r-1][c-1] == grid[r-1][c+1] == "S" and grid[r+1][c+1] == grid[r+1][c-1] == "M":
            ans += 1
        elif grid[r-1][c-1] == grid[r+1][c-1] == "M" and grid[r+1][c+1] == grid[r-1][c+1] == "S":
            ans += 1
        elif grid[r-1][c-1] == grid[r+1][c-1] == "S" and grid[r+1][c+1] == grid[r-1][c+1] == "M":
            ans += 1

print(ans)
