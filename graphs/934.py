class Solution(object):
    def shortestBridge(self, grid):
        n = len(grid)
        queue = []        
        def dfs(x, y):
            if 0 > x or x >= n or 0 > y or y >= n or grid[x][y] != 1:
                return
            grid[x][y] = 2
            queue.append([x, y, 0])
            dfs(x - 1, y)
            dfs(x, y - 1)
            dfs(x + 1, y)
            dfs(x, y + 1)
        
        flag = False
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    dfs(i, j)
                    flag = True
                    break
            if flag:
                break
        dirct = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        while len(queue) != 0:
            x, y, step = queue[0][0], queue[0][1], queue[0][2]
            queue.pop(0)
            for dx, dy in dirct:
                x1, y1 = x + dx, y + dy
                if 0 > x1 or x1 >= n or 0 > y1 or y1 >= n:
                    continue
                if grid[x1][y1] == 1:
                    return step
                if grid[x1][y1] == 0:
                    grid[x1][y1] = 2
                    queue.append([x1, y1, step + 1])⌈