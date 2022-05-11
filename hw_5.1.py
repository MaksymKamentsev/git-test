#Task2.
# Create a list that contains elements of integer type,
# then use the loop to change the type of these elements to a floating type.
#(Hint: use the built-in float () function).
c = []
n = int(input('Enter a number: '))
for i in range(1, n+1):
    c.append(float(i))
print(c)