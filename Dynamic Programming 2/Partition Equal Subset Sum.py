def helper(arr,target,n,memo):
    if target==0:
        return True
    if (n,target) in memo:
        return memo[(n,target)]
    if n==0:
        return False
    if arr[n-1]>target:
        return helper(arr,target,n-1,memo)
    include=helper(arr,target-arr[n-1],n-1,memo)
    exclude=helper(arr,target,n-1,memo)
    memo[(n,target)]=include or exclude
    return memo[(n,target)]
def canPartition(arr, n):
    # Write your code here.
    total=sum(arr)
    if total%2!=0:
        return False
    memo=dict()
    target=total/2
    return helper(arr,target,n,memo)