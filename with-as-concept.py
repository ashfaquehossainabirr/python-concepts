with open('./test/demo.txt', 'r') as file:
    contents = file.read()
    print(contents)


with open("./test/hi.txt", "r") as file:
    lines = file.readlines()

    for line in lines:
        print(line.strip()) # strip() removes the newline character



# Loops (Items with Index)

arr = ["A", "B", "C", "D", "E"]

for i, item in enumerate(arr):
    print(i+1, item)