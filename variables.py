full_name = "Ashfaque Hossain Abir"
age = 25
gpa = 3.2
isStudent = True

gpa_output = ["GPA:", str(gpa)]

print("Full Name: " + full_name) # Concatenation must be in string, otherwise this won't work
print(f"Age: {age}")
print(" ".join(gpa_output))

if isStudent:
    print("He is a student")
else:
    print("He isn't a student")