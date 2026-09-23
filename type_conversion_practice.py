# Practice: Type Conversion in Python

print(4 + 5)
print("Hello CodeMate!")

pi = 3.14159
print(pi)

first_number = 5
second_number = 6
print(first_number + second_number)
print(first_number * second_number)
print(first_number ** second_number)

# input() always returns a string, even if the user types a number
first_number = input("Please enter a number: ")
second_number = input("Please enter another number: ")

# print(first_number ** second_number)
# TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'str'
# Because ** requires numeric types, not strings

# print(first_number + second_number)
# Output: "56" -> this is string concatenation, not addition

print(int(first_number) + int(second_number))
# Converting to int allows real addition

print(float(first_number) + float(second_number))
# 11.0

days_in_february = 28

# print(days_in_february + "total days in February")
# TypeError: can't concatenate int and str directly

print(str(days_in_february) + " total days in February")
# Converting the int to a string allows concatenation
