# Declaring Variable
count = 0

# Function Creation
def increment():
    global count
    count += 1
    return count

increment()
increment()

# Display Output
print(f"Count: {increment()}")


# Scopes
def func():
    x = 2

    def innerScope():
        nonlocal x
        x = 5
    innerScope()

    print(f"Nonlocal: {x}")
func()

def func2():
    global gNum
    gNum = 15

func2()

print(f"Global: {gNum}")


# Lambda Function
marks = lambda marks, nums : marks + nums + 2

print(f"Marks: {marks(4, 2)}")


# Array
arr = [1, 2, 3, 4, 5]

# Loop
for num in arr:
    print(f"Loop: {num}")


# Math
a = 1
b = 2
c = 3

minimum_value = min(a, b, c)
maximum_value = max(a, b, c)

print(f"Minimum Value: {minimum_value}")
print(f"Maximum Value: {maximum_value}")


# Absolute (Positive) Value
negNum = -125

absoluteNum = abs(negNum)
print(f"Absolute: {absoluteNum}")


# Power
powerValue = pow(b, c)
print(f"Power: {powerValue}")


# Import Math
import math
sqrt_value = 81

sqrt_result = math.sqrt(sqrt_value)
print(f"Square Root of {sqrt_value} is {math.floor(sqrt_result)}")

decNum = 1.2

ceiling_num = math.ceil(decNum)
print(f"Ceiling Num of {decNum} is {ceiling_num}")


# Try Except
try:
    f = open("demo.txt")
    try:
        f.write("Lorem Ipsum")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file")



# Convert to 2 decimal place
price = 24

print(f"The price is ${price:.2f}")


# Dictionary
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car["color"] = "white"

print(f"Brand: {car['brand']}")
print(f"Color: {car.get('color')}")