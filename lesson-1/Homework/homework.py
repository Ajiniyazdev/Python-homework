# Problem 1
a = int(input('A side of square '))
P = 4 * a # The perimeter of square
S = a**2 # The area of square
print(S)
print(f'The area of square {S}, The perimeter of square {P}')

# Problem 2
import math
d = int(input('The diameter is '))
L = math.pi * d
print(L)

# Problem 3

a = int(input('Give me the first random number: '))
b = int(input('Give me the second random number: '))

print((a+b)/2)

# Problem 4
import math
a = int(input('Give me the first random number: '))
b = int(input('Give me the second random number: '))

print(a+b)
print(a*b)
print(math.sqrt(a), math.sqrt(b))
