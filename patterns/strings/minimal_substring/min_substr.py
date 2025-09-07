""" Write a function that takes in two inputs -- a string and a character set -- 
and returns the minimum-length substring which contains every letter of the character set at least once, 
in any order If you don't find a match, return an empty string """ 
def min_substring(input_str, char_set):
    ''' Helloe there ole 
       ['e', 'l' 'o'] '''
    lptr = 0
    char_map, window = {}, {}
    for ch in char_set:
        window[ch] = window.get(ch, 0) + 1
    have, need = 0, len(char_set)
    min_substr = ''
    min_left, min_right = 0, 0
    min_len = len(input_str)
    for rptr in range(len(input_str)):
        cur_char = input_str[rptr]
        char_map[cur_char] = char_map.get(cur_char, 0) + 1
        if cur_char in window and char_map[cur_char] == window[cur_char]:
            have += 1
        while have == need:
            if rptr - lptr + 1 < min_len:
                min_len = rptr - lptr + 1
                min_left, min_right = lptr, rptr
            left_char = input_str[lptr]
            char_map[left_char] = char_map.get(left_char, 0) - 1
            if left_char in window and char_map[left_char] < window[cur_char]:
                have -= 1
            lptr += 1
    return input_str[min_left : min_right + 1]
       

print(min_substring('Helloe thery' , 'elo'))
print(min_substring('a' , 'a'))    
print(min_substring('ADOBECODEBANC', 'ABC'))


