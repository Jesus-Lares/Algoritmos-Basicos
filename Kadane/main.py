array = [-3, -4, 5, -1, 2, -4, 6, -1]

def maximumSubarraySum(array):
    n=len(array)
    maxSum = -1e8 

    for i in range(0,n):
        currSum = 0
        for j in range(i,n):
            currSum +=array[j]
            if(currSum>maxSum):
                maxSum = currSum
    return maxSum


print(maximumSubarraySum(array))