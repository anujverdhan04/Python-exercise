class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        lists = list(itertools.chain(*matrix))
        lists.sort()
        n = len(lists)
        element = lists[k-1]
        return element
        