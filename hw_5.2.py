# Task3.
# Print Fibonacci numbers up to the entered number n,using cycles.
# (Sequence of Fibonacci numbers 0, 1, 1, 2, 3, 5, 8, 13, etc.)
x=0
b=1
n = int(input('Enter a number: '))
for i in range(0, n):
    print(x)
    x+=b
    print(b)
    b+=x
