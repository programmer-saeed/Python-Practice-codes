
a = int(input('Enter your first Number = '))  #In one line two input is a, b = input().split()
b = int(input('Enter your second Number = '))
print("\n")

print("First Number Enter  = ",a)
print("Second Number Enter = ",b)
print("\n")

sum = a + b
sub = a - b
mul = a * b
div = a / b
mod = a % b

print("Summation is = ",sum)
print("Subtraction is = ",sub)
print("Multiplier is = ",mul)
print("Division is = ",'%.4f' %div)     # For number of n value after decimal point using '%.nf' %variable
print("Modulus is = ",mod)

