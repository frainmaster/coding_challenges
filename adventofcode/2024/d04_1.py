def search_word(grid, word):
    """
    Search for a word in the given grid.
    Supports horizontal, vertical, and diagonal searches.

    :param grid: List of lists of strings, representing the word search grid.
    :param word: String, the word to search for.
    :return: List of tuples indicating the starting position and direction of the word.
    """
    rows, cols = len(grid), len(grid[0])
    word_length = len(word)
    directions = {
        "right": (0, 1),
        "down": (1, 0),
        "down-right": (1, 1),
        "up-right": (-1, 1),
        "left": (0, -1),
        "up": (-1, 0),
        "up-left": (-1, -1),
        "down-left": (1, -1),
    }

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def search_from(x, y, dx, dy):
        for i in range(word_length):
            nx, ny = x + i * dx, y + i * dy
            if not is_valid(nx, ny) or grid[nx][ny] != word[i]:
                return False
        return True

    results = []

    for r in range(rows):
        for c in range(cols):
            for direction, (dx, dy) in directions.items():
                if search_from(r, c, dx, dy):
                    results.append((r, c, direction))

    return results

# Example grid and word to search
with open('d04.txt') as f:
    grid = f.readlines()

word = "XMAS"

# Search for the word in the grid
found_positions = search_word(grid, word)
print(len(found_positions))

# if found_positions:
#     print(f"Word '{word}' found at:")
#     for pos in found_positions:
#         print(f"Start: ({pos[0]}, {pos[1]}), Direction: {pos[2]}")
# else:
#     print(f"Word '{word}' not found.")
