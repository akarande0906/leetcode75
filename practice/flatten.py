def flatten_concatenation(matrix):
    flat_list = []
    for row in matrix:
        flat_list.extend(row)
    return flat_list


def flatten_mixed_array(multi_array):
    flat_array = []
    def untangle_nested_array(elem, flat_array):
        if isinstance(elem, int):
            flat_array.append(elem)
        else:
            for a in elem:
                untangle_nested_array(a, flat_array)
        
    for a in multi_array:
        untangle_nested_array(a, flat_array)
    return flat_array


matrix = [
    [9, 3, 8, 3],
    [4, 5, 2, 8],
    [6, 4, 3, 1],
    [1, 0, 4, 5],
 ]
print (flatten_concatenation(matrix))


multi_array = [1, 2, [3, 4], [[[5,6]]]]
print (flatten_mixed_array(multi_array))
