# 2 - Further Data Types Operations
# ## 2.1 - Strings
# Strings in Python are arrays of bytes representing Unicode characters.
# Python does not have a character data type, a single character is simply a string with a length of 1.
# Strings can be enclosed in single quotes ('...') or double quotes ("...") with the same result.
# Operations on strings include:
# - Concatenation: "a" + "b" = "ab"
# - Multiplication: "a" * 3 = "aaa"
# - Lower and upper case: "abc".upper() = "ABC", "ABC".lower() = "abc"
# - Indexing: "abc"[1] = "b" (please note that Python uses 0-based indexing - first character is at index 0)
# - Slicing: "abc"[1:3] = "bc" (slicing returns a substring from the start index to the end index)
# - Length: len("abc") = 3
# - Splitting: "a,b,c".split(",") = ["a", "b", "c"]

our_basic_string = "Hello World!"

# TODO:
# - Add your name to the string
# - Print the string in upper case
# - Print the string in lower case
# - Print the first 5 characters of the string
# - Separate the string into two parts: "Hello" and "World!"
# - Print the length of the string

basic_string_with_name = ""
upper_case_string = ""
lower_case_string = ""
first_5_chars = ""
separated_string = []
string_length = 0

for key, value in {"basic_string_with_name": basic_string_with_name,
                   "upper_case_string": upper_case_string,
                   "lower_case_string": lower_case_string,
                   "first_5_chars": first_5_chars,
                   "separated_string": separated_string,
                   "string_length": string_length}.items():
    print(f"{key}: {value}")

# ## 2.2 - Lists
# Lists are used to store multiple items in a single variable.
# Lists are created using square brackets: ["apple", "banana", "cherry"]
# Operations on lists include:
# Accessing items: list[0] = "apple"
# Slicing: list[1:3] = ["banana", "cherry"]
# Length: len(list) = 3
# Adding items: list.append("orange") !!!Mutates the original object
# Removing items: list.remove("banana") !!!Mutates the original object
# Concatenate lists: ["apple", "banana", "cherry"] + ["orange", "lemon"]

# TODO:
# - Assign the first item of the list to a new variable
# - Assign all but the first item of the list to a new variable
# - Assign the length of the list to a new variable
# - Append "orange" to the list
# - Remove "orange" from the list
# - Concatenate the list with another list ["orange", "lemon"]

our_basic_list = ["apple", "banana", "cherry"]
first_item = None
all_but_first_item = []
list_length = None
appended_orange = None
removed_orange = None
concatenated_list = None

