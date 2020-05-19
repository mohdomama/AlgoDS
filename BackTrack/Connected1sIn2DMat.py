'''
Problem: https://www.geeksforgeeks.org/given-an-array-of-numbers-arrange-the-numbers-to-form-the-biggest-number/
Simple BackTrack
'''


def mark(a, n, m, visited, i, j):
    if i >= n or i < 0 or j >= m or j < 0:
        return

    if visited[i][j]:
        return

    if a[i][j] == 0:
        return

    visited[i][j] = True

    # Up
    mark(a, n, m, visited, i-1, j)
    # Down
    mark(a, n, m, visited, i+1, j)
    # Left
    mark(a, n, m, visited, i, j-1)
    # Right
    mark(a, n, m, visited, i, j+1)
    # UL
    mark(a, n, m, visited, i-1, j-1)
    # UR
    mark(a, n, m, visited, i-1, j+1)
    # DL
    mark(a, n, m, visited, i+1, j-1)
    # DR
    mark(a, n, m, visited, i+1, j+1)


def findIslands(a, n, m):
    islands = 0
    visited = [[False for j in range(m)] for j in range(n)]

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and a[i][j] == 1:
                islands += 1
                mark(a, n, m, visited, i, j)
    return islands


def main():
    a = [[1, 0, 0],
         [1, 1, 0],
         [0, 1, 1],
         [0, 0, 0],
         [1, 1, 0],
         [0, 0, 0],
         [1, 1, 0],
         ]
    n = 7
    m = 3
    print(findIslands(a, n, m))


if __name__ == '__main__':
    main()
