class Solution:
    def merge(self, interval: List[List[int]]) -> List[List[int]]:
        n = len(interval)
        interval.sort()
        ans = []
        for i in range(n):
            start = interval [i][0]
            end = interval [i][1]
            if ans and end <= ans[-1][1]:
                continue
            for j in range(i + 1, n):
                if interval[j][0] <= end:
                    end = max(end, interval[j][1])
                else:
                    break
            ans.append([start, end])
        return ans      