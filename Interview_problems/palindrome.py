def is_palindrome(input_string):
    left = 0
    right = len(input_string) - 1
    
    while left < right:
        # If characters at left and right indices are not equal, it's not a palindrome
        if input_string[left] != input_string[right]:
            return False
        left += 1
        right -= 1
    
    # If the loop completes without returning False, it's a palindrome
    return True

# Example usage
input_string = input("Enter a string: ")
result = is_palindrome(input_string)
print(result)
