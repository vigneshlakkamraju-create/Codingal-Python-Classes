def add(x, y):
    return x + y

def subtract (x, y):
    return x - y

def multiply (x, y):
    return x * y

def divide (x, y):
    return x / y


number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

print("Sum :", add(number_1, number_2))
print("Difference :", subtract(number_1, number_2))
print("Product :", multiply(number_1, number_2))
print("Quotient :", divide(number_1, number_2))