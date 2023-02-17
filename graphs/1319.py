class Solution(object):
    def makeConnected(self, n, connections):
        global cnt
        cnt = 0
        mat = {i: [] for i in range(n)}
        for i in range(len(connections)):
            v1, v2 = connections[i][0], connections[i][1]
            mat[v1].append(v2)
            mat[v2].append(v1)
        used = [0 for _ in range(n)]
        def dfs(v, pr=-1):
            global cnt
            used[v] = 1
            for u in mat[v]:
                if used[u] and u != pr:
                    cnt += 1
                else:
                    if u != pr:
                        dfs(u, v)
        cnt_cmp = 0
        for i in range(n):
            if not used[i]:
                cnt_cmp += 1
                dfs(i)
        cnt //= 2
        if cnt >= cnt_cmp - 1:
            return cnt_cmp - 1
        return -1