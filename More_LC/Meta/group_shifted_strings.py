'''
Given an array of strings: The shifting code is how many characters are shifted to get the next character
For e.g. ADE has shifting seq of 3,1 (3 letters to get to D and 1 letter to get to E)
Find the shifting seq of all strings and group them by shifting sequence:
[['ABD', 'BCE'], ['AC', 'YA']]
'''

def groupShiftedStrings(string_array):
    group_map = {}
    for string in string_array:
        if len(string) <= 1:
            if not '' in group_map:
                group_map[''] = []
            group_map[''].append(string)
            continue
        shift_string = ''
        for c in range(1, len(string)):
            shift_code = ord(string[c]) - ord(string[c-1])
            shift_code = shift_code if shift_code > 0 else 26 + shift_code # Handle rotation
            shift_string += str(shift_code) + ','
        if not shift_string in group_map:
            group_map[shift_string] = []
        group_map[shift_string].append(string)
    return_array = []
    for k, v in group_map.items():
        return_array.append(v)
    return return_array

print(groupShiftedStrings(['abd', 'bce', 'ac', 'ya', 'h', 'p']))

