class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        A.sort(reverse=True)
        B.sort(reverse=True)
        
        results = []
        
        # Collect the initial top combinations
        for i in range(len(A)):
            for j in range(len(B)):
                if len(results) < C:
                    results.append(A[i] + B[j])
                else:
                    # If the current sum is less than the smallest in results, break
                    if A[i] + B[j] < min(results):
                        break
                    else:
                        results.append(A[i] + B[j])
                        # Remove the smallest element to keep the size to C
                        results.sort(reverse=True)
                        results = results[:C]
        
        return results
