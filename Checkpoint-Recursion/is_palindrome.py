def is_palindrome(word):
    # Base case: an empty word or a word containing a single character is a palindrome
    if len(word) <= 1:
        return True
    
    # Check if the first and last characters are equal
    if word[0] == word[-1]:
        # Recursively check the rest of the word
        return is_palindrome(word[1:-1])
    
    # Base case: if a word is not a palindrome(doesn't meet the previous condition) then surely it is NOT a palindrome
    return False