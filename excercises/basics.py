# 1 - Python Basics
## 1.1 - Variables
# Variables are used to store data. A variable is created the moment you first assign a value to it.
# Variables do not need to be declared with any particular type, and can even change type after they have been set.
# Variable names can contain letters, our_numbers, and underscores, but cannot start with a number. A whitespace is not
# allowed (is interpreted as a start of new object).
# Python is case-sensitive, so "a" and "A" are different variables.

# TODO: Create a variable called "name" and set it to ANY name.
# TODO: Create a variable called "date_birth" and set it to ANY date of birth (use format YYYY_MM_DD).
name = ""
date_birth = ""

for key, value in {"name": name, "date_birth": date_birth}.items():
    print(f"{key}: {value}")

## 1.2 - Data Types
# Python has several data types (such as
# Data types can be either abstract or concrete
# While concrete data type define a specific type of data, abstract data types are used to define a data structure,
# i.e. a way you can store items and organize them in memory.

# TODO: Create following variables and set as appropriate data type:
# - "age" and set it to an integer
# - "height" in meters and set it to a float
# - "is_student" and set it to a boolean (True/False)
# - "team" (list of colleagues from the same team, each of them is an item in the list)

age = 0
height_m = 0.0
weight_kg = 0.0
is_student = False

for key, value in {"age": age,
                   "height_m": height_m,
                   "weight_kg": weight_kg,
                   "is_student": is_student}.items():
    print(f"{key}: {value}")


## 1.3 - Operators
# One of the essential building blocks of programming is the ability to perform operations on data.
# Operators are used to perform operations on variables and values.
# Python has several types of operators, including:
# - Arithmetic operators: + (add), - (subtract), * (multiply), / (divide),
#   % (modulo - returns remainder after division, ** (exponentiation) , // (whole number division)
# - Assignment operators: = (assign value), += (add and assign), -= (subtract and assign), *= (multiply and assign),
# - Comparison operators: == (equal), != (not equal), > (greater than), < (less than), >= (greater than or equal to),
# - Logical operators: and, or, not

# TODO: Perform the following operations:
# - Add 2 to the "age" variable
# - Create a new variable called BMI and compute the value (formula is BMI = weight[kg] / height[meters]^2)
# - Check if the "age" is greater than 18
# - Check if the age is an odd number (hint: use modulo operator)
# - Check how many times did the person celebrate 10-year-milestone birthday (hint: use whole number division)
# - Check if the person is a student and is younger than 18

add_age_2 = age
bmi = 0
age_greater_18 = False
age_odd = False
celebrated_10_years = False
student_and_younger_than_18 = False

for key, value in {"add_age": add_age_2,
                   "bmi": bmi,
                   "age_greater_18": age_greater_18,
                   "age_odd": age_odd,
                   "celebrated_10_years": celebrated_10_years,
                   "student_and_younger_than_18": student_and_younger_than_18}.items():
    print(f"{key}: {value}")
