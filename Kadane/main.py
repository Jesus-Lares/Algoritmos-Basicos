array = [-3, -4, 5, -1, 2, -4, 6, -4,5]

"""
def maximumSubarraySum(array):
    n=len(array)
    maxSum = -1e8 
    arraySum=[]

    for i in range(0,n):
        currSum = 0
        for j in range(i,n):
            currSum +=array[j]
            if(currSum>maxSum):
                arraySum=array[i:j+1]
                maxSum = currSum
          

    return maxSum,arraySum

"""
def maximumSubarraySum(array):
    n = len(array)
    maxSum = -1e8
    currSum = 0
    cont=0
    arraySum=[]

    for i in range(0, n):
        currSum = currSum + array[i]
        if(currSum > maxSum):
            arraySum=array[cont:i+1]
            maxSum = currSum
        if(currSum < 0):
            currSum = 0
            cont=i+1
      
    return maxSum,arraySum 



print(maximumSubarraySum(array))
