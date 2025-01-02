def dp(weights, values, W):

	m = len(weights)
	memo = [float('inf')] * (100000 + 1)
	memo[0] = 0

	for i in range(m):
		weight = weights[i]
		value  = values[i]

		for w in range(weight, 100001):
			memo[w] = min(memo[w], memo[w-weight] + value)

	res = float('inf')
	for w in range(W, 100001):
		res = min(res, memo[w])

	return res

def main():

	m, n = map(int, input().split())
	H = list(map(int, input().split()))
	D = list(map(int, input().split()))

	total = 0
	for d in D:
		total+=d

	r = dp(H,D,n)
	print(total-r)

if __name__ == '__main__':
	main()


# Case 1:
# 6 100
# 1 1 1 1 100 99
# 10 8 10 10 2 1
# 39
# Case 2:
# 6 100
# 1 1 1 2 100 99
# 10 8 10 1 5 1
# 33
