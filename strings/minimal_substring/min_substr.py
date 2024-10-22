""" Write a function that takes in two inputs -- a string and a character set -- 
and returns the minimum-length substring which contains every letter of the character set at least once, 
in any order If you don't find a match, return an empty string """ 
def min_substring(input_str, char_set):
    ''' Helloe there ole 
       ['e', 'l' 'o'] '''

    if not input_str:
       return ''
    lptr = 0
    while input_str[lptr] not in char_set:
       lptr += 1
    cur_str = ''
    min_str = ''
    rptr = lptr
    while lptr <= rptr and rptr < len(input_str):
       cur_str = ''
       chars = set(char_set)
       for rptr in range(lptr, len(input_str)):
          if input_str[rptr] in chars:
              chars.remove(input_str[rptr])
              if not chars or not len(chars):
                  cur_str = input_str[lptr:rptr+1]
                  print ('Cur STR: ' + cur_str)
                  if not min_str or len(cur_str) < len(min_str): 
                      min_str = cur_str
                  lptr += 1
                  rptr = lptr
                  break
    return min_str  
       

print(min_substring('Helloe thery' , ['e','l','o']))    
print(min_substring('a' , ['a']))    


