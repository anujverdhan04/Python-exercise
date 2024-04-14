class Solution(object):
    def longestMountain(self, arr):
        n = len(arr)
        max_length = 0
        up = down = 0

        for i in range(1, n):
            if (down and arr[i] > arr[i - 1]) or arr[i] == arr[i - 1]:
                up = down = 0

            up += arr[i] > arr[i - 1]
            down += arr[i] < arr[i - 1]

            if up and down:
                max_length = max(max_length, up + down + 1)

        return max_length
      