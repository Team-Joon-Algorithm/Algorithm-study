class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 1:
                return
            grid[i][j] = 1
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 or i == len(grid)-1 or j == 0 or j == len(grid[0])-1:
                    if grid[i][j] == 0:
                        dfs(i, j)

        result = 0
        for i in range(1, len(grid)-1):
            for j in range(1, len(grid[0])-1):
                if grid[i][j] == 0:
                    dfs(i, j)
                    result += 1

        return result