# Coding Exercise 1
# Define a function that has two parameters,
# year_of_birth and current_year .
# The current_year parameter should be a default parameter with the current year as a default value.
# The function should calculate and return the age of the user given the year of birth and the current year.
# Note: It is enough to define the function for this exercise -no need to call it.

# age_input = int(input("Enter your birth year: "))
#
# def age(year_of_birth, current_year=2023):
#     calculate = current_year - int(year_of_birth)
#     return calculate
#
#
# current_age = age(age_input)
# if current_age > 120:
#     print("You're too old")

# Coding Exercise 4
# Write a program that gets a list of names from the user and returns the number of names given.
# You are encouraged to use a function. Here is how the program would work:

def count_names(user_input):
    items = user_input.split(",")
    return len(items)

names =  input("Enter names separated by commas: ")
no_names = count_names(names)
print(no_names)


