
def make_step(steps, matrix, grid):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == steps:
                if i > 0 and matrix[i - 1][j] == 0 and grid[i - 1][j] == 0:
                    matrix[i - 1][j] = steps + 1
                if j > 0 and matrix[i][j - 1] == 0 and grid[i][j - 1] == 0:
                    matrix[i][j - 1] = steps + 1
                if i < len(matrix) - 1 and matrix[i + 1][j] == 0 and grid[i + 1][j] == 0:
                    matrix[i + 1][j] = steps + 1
                if j < len(matrix[i]) - 1 and matrix[i][j + 1] == 0 and grid[i][j + 1] == 0:
                    matrix[i][j + 1] = steps + 1
def pathFinder(maze, start, end):
    grid = []
    i = 0
    for subList in maze.maze:
        grid.append([])
        for obj in subList:
            grid[i].append(int(obj.isWall))
            # print(grid)
        i += 1

    matrix = []
    for i in range(len(grid)):
        matrix.append([])
        for j in range(len(grid[i])):
            matrix[-1].append(0)
    i, j = start
    matrix[i][j] = 1

    steps = 0
    while matrix[end[0]][end[1]] == 0:
        steps += 1
        make_step(steps, matrix, grid)

    i, j = end
    steps = matrix[i][j]
    path = [(i, j)]
    while steps > 1:
        if i > 0 and matrix[i - 1][j] == steps - 1:
            i, j = i - 1, j
            path.append((i, j))
            steps -= 1
        elif j > 0 and matrix[i][j - 1] == steps - 1:
            i, j = i, j - 1
            path.append((i, j))
            steps -= 1
        elif i < len(matrix) - 1 and matrix[i + 1][j] == steps - 1:
            i, j = i + 1, j
            path.append((i, j))
            steps -= 1
        elif j < len(matrix[i]) - 1 and matrix[i][j + 1] == steps - 1:
            i, j = i, j + 1
            path.append((i, j))
            steps -= 1

    return path


