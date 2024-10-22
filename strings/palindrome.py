import re

def palindrome(str):
    str2 = re.sub(r'\W+', '', str).lower()
    lptr = 0
    rptr = len(str2) - 1
    while lptr < rptr:
       if str2[lptr] != str2[rptr]:
          return False
       lptr += 1
       rptr -= 1
    return True

def palindrome_2(str):
    str = str.lower()
    lptr = 0
    rptr = len(str) - 1
    while lptr < rptr:
       while not str[lptr].isalnum():  
          lptr += 1
       while not str[rptr].isalnum(): 
          rptr -= 1
       if str[lptr] != str[rptr]:
         return False
       lptr += 1
       rptr -= 1
    return True


str = "Madam, I'm Adam!"
print(palindrome(str))
print(palindrome_2(str))
 
str = "Sure I am ruse"
print(palindrome(str))
print(palindrome_2(str))

str = "I am not ton mai"
print(palindrome(str))
print(palindrome_2(str))
