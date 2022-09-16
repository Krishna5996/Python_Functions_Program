def memoize_factorial(f):
	memory = {}
	def inner(num):
		if num not in memory:	 
			print("g ")
			memory[num] = f(num)
		return memory[num]
	return inner
	
@memoize_factorial
def calculate_factorial(num):
	if num == 1:
		return 1
	else:
		return num * calculate_factorial(num-1)

print(calculate_factorial(5))
