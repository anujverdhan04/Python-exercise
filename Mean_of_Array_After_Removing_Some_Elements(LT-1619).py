class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n = len(arr)
        sum = 0
        for i in range(n //20 , n-n//20):
            sum+=arr[i]
        return sum / (n - n // 10) 
        