class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        st = set()
        for i in  range(n):
            for j in range(i+1 , n):
                hashset = set()
                for k in range(j+1,n):
                    sum_ = nums[i] + nums[j]
                    sum_ += nums[k]
                    l = target - sum_
                    if l in hashset:
                        temp = [ nums[i] , nums[j] , nums[k] , l]
                        temp.sort()
                        st.add(tuple(temp))
                    hashset.add(nums[k])
        ans = [list(t) for t in st]
        return ans                


        