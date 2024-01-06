
def maximumProfit(arr):
	#Implement Your Function here
	arr.sort()
	ans=float(-1)
	n=len(arr)
	for i in range(n):
		ans = max(ans, arr[i] * (n - i))
	return ans
n = int(input())
arr = [int(ele) for ele in input().split()]
ans = maximumProfit(arr)
print(ans)