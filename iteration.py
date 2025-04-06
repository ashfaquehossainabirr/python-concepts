# Iterating over a list

fruits = ["Apple", "Orange", "Banana", "Mango", "Pineapple", "Watermelon"]

for fruit in fruits:
    print(fruit)


# Iterating over a dictionary

student1 = {
    "name": "Ashfaque Hossain Abir",
    "age": 25,
    "gpa": 3.5
}

for key, value in student1.items():
    print(f"{key}: {value}")


# Iterating over a set

total_sum = 0

nums = {1, 2, 3, 4, 5}

for num in nums:
    total_sum += num

print(total_sum)



# While Loop

count = 0

while count <= 5:
    print("Count: " + str(count))
    count += 1



running = True

count = 0

while running:
    print("Count: " + str(count))
    count += 1

    if count >= 5:
        break



count = 0

while count < 5:
    count += 1

    if count == 3:
        continue

    print("Count: " + str(count))
