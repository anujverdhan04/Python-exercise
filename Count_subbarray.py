def solveaa (self, A, B):
        n= len(A)
        count =0 
        for i in  range(n):
            xxor = 0
            for j in range(i,n):
                xxor = xxor ^ A[j]
                if(xxor  == k):
                    count +=1    
        return count        

if __name__ == "__main__":
       A = [4, 2, 2, 6, 4]
       k = 6
       ans = solveaa (A, k)
       print("The number of subarrays with XOR k is:", ans)
