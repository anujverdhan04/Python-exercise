
def validMountainArray(self, arr):
    n = len(arr)
    if (len(arr) < 3):
                return False
    for i in range(len(arr)):
            if (arr[i]<arr[i+1]) and (arr[i-1]<=arr[i]):
                return True
            elif(arr[n-1] < max(arr)) :
                return True
            else:
                return False    

result = validMountainArray(None,[0,2,3,4,5,2,1])
print(result)  
      
        