def has_unique_characters(input_string):
    char_set = set()  # Create an empty set to store encountered characters
    for char in input_string:
        if char in char_set:
            return False  # If the character is already in the set, the string does not have all unique characters
        char_set.add(char)  # Add the character to the set
    return True  # If the loop completes, the string has all unique characters

input_string = input("Enter a string: ")
if has_unique_characters(input_string):
    print("The string has all unique characters.")
else:
    print("The string does not have all unique characters.")





