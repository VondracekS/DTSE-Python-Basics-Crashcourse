# 3 Conditions, Iterations and Functions


## 3.1
# The real power of programming is in the ability to repeat a task multiple times. This is called iteration.
# In Python, we can iterate over a sequence of items using a for loop.
# The for loop iterates over a sequence of items and executes the block of code inside the loop
# once for each item in the sequence. The sequence can be a list, a tuple, a string, a range, or any other iterable object.
# Here is an example of a for loop that iterates over a list of our_numbers and prints each number to the console:

for i in range(10):
    print(i)


## 3.2
# One of the key programming concepts is the ability to perform different actions based on a condition.
# IN python, we use the if statement to perform a certain action based on a condition.
# If the condition is True, the code inside the if statement is executed. If the condition is False, the code is skipped.
# In the followwing example, we iterrate over elements of a list and print whether the number is even or odd and how many digits it has.

our_numbers = [1, 15, 26, 78, 256, 789, 2267]
for num in our_numbers:
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

    if num < 10:
        print(f"{num} is a one-digit number")
    elif num > 10 and num < 100:
        print(f"{num} is a two-digit number")
    elif num > 100 and num < 1000:
        print(f"{num} is a three-digit number")
    else:
        print(f"{num} is a four-digit number")

## 3.3
# Another way of iteration is the so-called while loop.
# The while loop repeats a block of code as long as a specified condition is True.
# The following example shows how to use a while loop to move all components from our_numbers list to a new list
# called numbers_moved.

numbers_moved = []
while len(our_numbers) > 0:
    numbers_moved.append(our_numbers.pop(0))
    print(numbers_moved[-1])

## 3.4
# Functions are a way to organize code into reusable blocks.
# Each function has its defined name, input parameters, and output value.
# In the following example, I create a simple function that indicates whether input number is even

def is_even_number(number):
    if number % 2 == 0:
        return True
    return False


# I create another function to print how many digits the number has


def print_n_digits(number):
    return number//10


# Now we can combine these functions to print whether the number is even and how many digits it has
def print_number_info(numbers_list):
    for num in numbers_list:
        print(f"The number {num} is even: {is_even_number(num)} and has {print_n_digits(num)} digits")
        # Note that I use an f-string to print variables, syntax is rather simple: f"Variable has value: {variable}"



# TODO:
# - Create a function that takes a string as input and returns the number of characters in the string
# - Create a function that takes a list of numbers as input and returns the sum of the numbers
# - Create a function that takes a list of numbers as input and returns the mean (using function defined above)


def count_characters(string):
    pass

print(count_characters("blabla"))


def sum_numbers(numbers_list):
    sum_result = 0
    # TODO: Your iterations
    return sum_result

print(sum_numbers([1, 2, 3, 4, 5]))

def average_numbers(numbers_list):
    sum = sum_numbers(numbers_list)
    # TODO:
    pass

print(average_numbers([1, 2, 3, 4, 5]))
