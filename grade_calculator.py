# Author: Brother Godstime
# Date: 2025-07-15
# Purpose: Grade Calculator
# This is a program to determine grade letters with +/- based on a grade input.

# Prompt the user for a score
grade = int(input("What is your grade percent "))

if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else:
    letter = "F"

# Determine if the grade has a plus or minus
sign = ""

last_digit = grade % 10

if last_digit >= 7:
    sign = "+"
elif last_digit < 3:
    sign = "-"
else:
    sign = ""

# Handle special cases for A+
if grade > 93:
    sign = ""

# Handle special cases for F+ and F-
if letter == "F":
    sign = ""

# Combine the letter and sign to form the final grade
print(f"Your letter grade is: {letter}{sign}")

if grade >= 70:
    print("Congratulations! You passed the class.")
else:
    print("Stay focused and keep trying. You can improve your grade!")