
'''
Look and Say sequence: 
First element is 1, second one is One 1, third is 2 ones, fourth is one two and one one
1
11
21
1211
111221
312211
13112221
1113213211
31131211131221
13211311123113112211
'''

def look_and_say_sequence(input):
    value = '1'
    for i in range(1, input+1):
        print (value)
        value = construct_value(value)

def construct_value(input):
    output = ''
    if len(input) == 1:
        return '1' + input
    else:
        count = 1
        cur_char = input[0]
        for c in range(1, len(input)):
            if cur_char == input[c]:
                count += 1
            elif cur_char != input[c]:
                output = output + str(count) + cur_char
                count = 1
                cur_char = input[c]
            if c == len(input) - 1:
                if cur_char == input[c]:
                    output = output + str(count) + cur_char
                else:
                    output = output + str(1) + input[c]
    return output   

look_and_say_sequence(8)

