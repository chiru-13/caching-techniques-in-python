def fibonacci(n, cache={}):
	if n in cache:
		return cache[n]
	if n <=1:
		result = 1
	else:
		result = fibonacci(n-1) + fibonacci(n-2)
	cache[n] = result
	return result

print(fibonacci(15)) 