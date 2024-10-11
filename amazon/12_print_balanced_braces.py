def print_all_braces_rec(n, left_count, right_count, output, result):
    if left_count >= n and right_count >= n:
        result.append("".join(output))

    if left_count < n:
        output.append('{')
        print ('Lout: ' + str(output))
        print_all_braces_rec(n, left_count + 1,
                   right_count, output, result)
        output.pop()

    if right_count < left_count:
        output.append('}')
        print ('Rout: ' + str(output))
        print_all_braces_rec(n, left_count,
                   right_count + 1, output, result)
        output.pop()

def print_all_braces(n):
    result = []
    output = []
    print_all_braces_rec(n, 0, 0, output, result)

    return result


print(print_all_braces(3))
