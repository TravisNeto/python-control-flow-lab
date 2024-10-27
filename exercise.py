# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

def check_letter():
    letter = input("Please enter a letter (a-z or A-Z): ").strip()

    if len(letter) != 1 or not letter.isalpha():
        print("Invalid entry. Please enter a single alphabetical letter.")
        return

    letter_lower = letter.lower()

    if letter_lower in 'aeiou':
        print(f"The letter {letter} is a vowel.")
    else:
        print(f"The letter {letter} is a consonant")

# Call the function
check_letter()



# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

def check_voting_eligibility():
    voting_age = 18

    age_input = input("Please enter your age:")

    try:
        age = int(age_input)

        if age <0:
            print("Age cannot be negative. Please enter a valid age")
            return

        if age >= voting_age:
            print("You are eligible to vote")
        else:
            print("You ar enot eligible to vote")

    except ValueError:
        print("Invalid input. Please enter a valid age")

# Call the function
check_voting_eligibility()



# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

def calculate_dog_years():
    age_input = input("Input a dog's age:")

    try:
        dog_age = int(age_input)
        
        if dog_age < 0:
            print("Age cannot be negative. Please enter a valid age")
            return

        if dog_age <= 2:
            dog_years = dog_age * 10
        else:
            dog_years = 20 + (dog_age - 2) * 7

        print(f"the dog's age in dog years is {dog_years}")

    except ValueError:
        print("Invalid input. Please enter a valid dog's age")
        

# Call the function
calculate_dog_years()



# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

def weather_advice():
    cold_input = input("Is it cold? (yes/no): ").strip().lower()

    raining_input = input("Is it raining? (yes/no): ").strip.lower()

    if cold_input not in ['yes', 'no'] or raining_input not in ['yes', 'no']:
        print("Invalid input. Please respond with 'yes' or 'no'")
        return

    is_cold = cold_input == 'yes'
    is_raining = raining_input == 'yes'

    if is_cold and is_raining:
        print("Wear a waterproof coat")
    elif is_cold and not is_raining:
        print("Wear a warm coat")
    elif not is_cold and is_raining:
        print("Carry an umbrella")
    else:
        print("Wear light clothing")

# Call the function
weather_advice()



# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

def determine_season():
    month_input = input("Enter the month of the year (Jan - Dec): ").strip().capitalize()

    day_input = input("Enter the day of the month: ").strip()

    try:
        day = int(day_input)
        if day < 1 or day > 31:
            print("Invalid day. Please enter a valid day of the month (1-31) ")
            return
        except ValueError:
            print("Invalid input. Please enter a valid day")
            return

        if month_input == "Dec":
            season = "Winter" if day >= 21 else "Fall"
        elif month_input == "Jan" or month_input == "Feb":
            season = "Winter"
        elif month_input == "Mar":
            season = "Spring" if day < 20 else "Winter"
        elif month_input == "Apr" or month_input == "May":
            season = "Spring"
        elif month_input == "Jun":
            season = "Summer" if day >= 21 else "Spring"
        elif month_input == "Jul" or month_input "Aug":
            season = "Summer"
        elif month_input == "Sep":
            season = "Fall" if day < 22 else "Summer"
        elif month_input == "Oct" or month_input == "Nov":
            season = "Fall"
        else:
            print("Invalid month. Please enter a valid month (Jan - Dec) ")
            return

        print(f"{month_input} {day} is in {season}")

# Call the function
determine_season()
