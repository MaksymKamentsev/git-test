#Task1.
# Write a script that will calculate the factorial of the entered number
# without using recursion

def factorial(n):
	result = 1
	for i in range(1,n+1):
		result = result*i
	return result

n = int(input('Enter a number: '))
result = factorial(n)
print(n,'! = ',result,sep="")