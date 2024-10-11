def are_anagrams(str1, str2):
    if not str1 and not str2:
        return True
    elif str1 and str2 and len(str1) != len(str2):
        return False
    elif str1 and str2:
        map = {}
        for c in str1:
            map[c] = map.get(c, 0) + 1
        print (map)
        for c in str2:
            if not map[c]:
               return False
            map[c] -= 1
            if map[c] == -1:
                return False
            
    return True


print(are_anagrams('abcdef', 'fedabc'))
print(are_anagrams('abbdef', 'ffdabc'))
