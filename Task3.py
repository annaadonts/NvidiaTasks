# Cars are the most popular way of transportation in the USA and many countries around the world. It's only natural that people want to find a way to standout from the crowd when they buy their new vehicle. One of the ways to have some fun with your car is to order what is called a "personalized plate", a special type of vehicle registration plate with a funny word or a number which is important for the driver.
# With a system like that there are always ways for abuse, so local or federal governments like to introduce lists or requirements. It can be a list like this:
# ●Plates are required to start with at least two letters.
# ●Needs to contain a minimum of 2(letters or numbers) characters and a maximum of 6.
# ●Numbers should only be used at the end of the plate, so GTL42 is ok, but GPDS2X is not.
# ●First number used must not be a '0'.
# ●No whitespace characters or punctuation marks are allowed.

# In this program you will need to implement a validator for personalized plates. It will ask users to enter plate word/number sequence they want to get, and output "Valid plate!" or "Sorry, invalid plate" in the appropriate cases.

# As we like to have our code reusable, we want to implement this program via a number of validator functions. At the very least we want to have a 'main' entry point function and internal 'is_plate_valid' function, that accepts plates in string type and returns bool after checking all the requirements. You can implement additional smaller validation functions to structure your code better.


import re

def is_plate_start_with_letters(plate: str) -> bool:
    return all(char.isalpha() for char in plate[:2])

def is_plate_length_valid(plate: str) -> bool:
    return 2 <= len(plate) <= 6 and plate.isalnum()

def is_numbers_at_end(plate: str) -> bool:
    match = re.match(r'([A-Z]+)(\d+)$', plate)
    if match:
        letters, numbers = match.groups()
        return True
    return False

def is_plate_valid(plate: str) -> bool:
    plate = plate.upper()
    if not is_plate_length_valid(plate):
        return False
    if not is_plate_start_with_letters(plate):
        return False
    if not is_numbers_at_end(plate):
        return False
    if plate[0] == '0':
        return False
    return True

def validate_personalized_plate() -> None:
    plate = input("Enter the plate: ").upper()
    if is_plate_valid(plate):
        print("Valid plate!")
    else:
        print("Sorry, invalid plate.")

if __name__ == "__main__":
    validate_personalized_plate()
