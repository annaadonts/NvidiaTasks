# Let’s imagine that you’re visiting a country where it’s a custom to have breakfast at 7:00 to 8:00 window, lunch at 12:00 to 13:00, and finish with dinner at 18:00 to 19:00. Let’s create a helper for us to check if it’s time to have a meal and what kind of meal it will be. 

# Implement a program that asks the user to enter a time and outputs “time for breakfast”, “time for launch”, “time for dinner”. 
# If it’s not yet time to eat, just don’t output anything.

# Time windows specified above are inclusive, so 12:00, 12:05 and 13:00 - are all good times to get a launch according to our helper. 
# Accepted time format will be a 24 hour time, so something like *:** (7:00) or **:** (07:00) should work.
# To make our code a bit more reusable, we want to structure our program to also include a “time_convert” function, that accepts time in the described string format and will return it back in float format. So for the “9:30” input it will return “9.5”. This useful function should be a part of the algorithm that produces the final result, so we will call this function at one point of our program.

# Let’s assume that inputs are valid, we don’t need to validate them.

def time_convert(time_str):
    hour, minute = map(int, time_str.split(':'))
    return hour + minute / 60

def meal_time(time_float):
    if 7 <= time_float < 8:
        return 'breakfast'
    elif 12 <= time_float < 13:
        return 'lunch'
    elif 18 <= time_float < 19:
        return 'dinner'
    else:
        return None

def main():
    user_time = input('Enter time in : format: ')
    time_float = time_convert(user_time)
    meal = meal_time(time_float)
    if meal:
        print(f'It\'s time for {meal}!')

if __name__ == '__main__':
    main()

