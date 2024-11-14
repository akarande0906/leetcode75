# Function to check if a string is a palindrome
def isPalindrome(s, final_list):
    left, right = 0, len(s) - 1 
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1 
        right -= 1
    final_list.append(s)
    return True

# Recursive function to generate subsequences
# and count palindromic ones
def generateSubseq(s, i, curr, final_list):
  
    # Base case: if we've considered all characters
    if i == len(s):
        return 1 if isPalindrome(curr, final_list) and curr else 0

    # Include the current character in the subsequence
    res1 = generateSubseq(s, i + 1, curr + s[i], final_list)

    # Exclude the current character from the subsequence
    res2 = generateSubseq(s, i + 1, curr, final_list)

    # Return the total count of palindromic subsequences found
    return res1 + res2

# Function to count the number of palindromic subsequences
# in a given string
def countPS(s):
    final_list = []
    total = generateSubseq(s, 0, "", final_list)
    print (final_list)
    return total

# Driver code
s = "tsetse" 
#s = "geeksforgeeks" 
print(countPS(s))
