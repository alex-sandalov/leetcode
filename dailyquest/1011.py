class Solution(object):
    def shipWithinDays(self, weights, days):
        n = len(weights)

        def check(mid):
            cur = 0
            cnt = 0
            for i in range(n):
                if weights[i] + cur > mid:
                    cur = 0
                    cnt += 1
                if weights[i] > mid:
                    return False
                cur += weights[i]
            return cnt < days

        def binary_search():
            l = 0
            r = sum(weights)
            while l < r:
                mid = (l + r) // 2
                if check(mid):
                    r = mid
                else:
                    l = mid + 1
            return (l + r) // 2
        return binary_search()