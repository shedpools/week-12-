# Objective:
# Students will learn how to compare values using Python’s comparison operators and interpret Boolean results.

# Topics Covered:
# ==, !=, >, <, >=, <=

# Key Notes:

# Comparison operators compare two values and return either True or False.

# Remember: = is assignment, while == is comparison.

a = 3
b = 4

print(a == b)   # False
print(a != b)   # True
print(a > b)    # False
print(a < b)    # True
print(a >= b)   # False
print(a <= b)   # True


#predict the output of the following comparisons:
10 > 5 #true
7 == 2 * 3 + 1 #true
8 != 8 #false
4 <= 2 + 2 #true

# Write 3 examples that result in True and 3 that result in False.
2 > 1 #true
3 == 3 #true
1 < 2 #true
1 > 1 #false
2 == 4 #false
7 > 8 #false
# Create a simple grade-checking condition:

# practice problem :
# where a student must check if their score is greater than or equal to 60 to pass a test.# The password must be at least 8 characters long and contain at least one digit.password = "mypassword1"
score = int(input("enter your score:"))
if score >= 60:
    print("u passed yo")
else:
    print("baka </3")

password = input("enter yo password:")
if len(password) >= 8 and any(char.isdigit() for char in password):
    print("password is valid")
else:
    print("ts password invalid")