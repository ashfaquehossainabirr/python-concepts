# Concept: List, Tuple and Sets (With List methods)


# fruits = ("Apple", "Orange", "Banana", "pineapple", "Mango", "Watermelon")

# print(type(fruits)) # Tuple

# fruits = ["Apple", "Orange", "Banana", "pineapple", "Mango", "Watermelon"]

# print(type(fruits)) # List or Array

# fruits = {"Apple", "Orange", "Banana", "pineapple", "Mango", "Watermelon"}

# print(type(fruits)) # Set



fruits = ["Apple", "Orange", "Banana", "pineapple", "Mango", "Watermelon"]

fruits.append("Lemon") # Push Method
fruits.remove("Mango") # Remove Item
fruits.insert(4, "Mango") # Insert item at index
fruits.sort() # Sort the list
fruits.reverse() # Reversing the list
lemon_index = fruits.index("Lemon") # Index of item "Lemon"
count_item = fruits.count("Apple")

print(fruits)
print(len(fruits))
print("Lemon: " + str(lemon_index))
print("Apple Count: " + str(count_item))