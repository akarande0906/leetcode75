

def countDistinctTriangles(arr):
    triangle_set = set()
    for a in arr:
        if not tuple(sorted(a)) in triangle_set:
            triangle_set.add(tuple(sorted(a)))
    return len(triangle_set)

# def countDistinctTriangles(arr):
#     triangle_set = set()
#     for a in arr:
#         triangle_str = ''.join(str(i) for i in sorted(a))
#         if not triangle_str in triangle_set:
#             triangle_set.add(triangle_str)
#     return len(triangle_set)


print (countDistinctTriangles([(7, 6, 5), (5, 7, 6), (8, 2, 9), (2, 3, 4), (2, 4, 3)]))
print (countDistinctTriangles([(3, 4, 5), (8, 8, 9), (7, 7, 7)]))
print (countDistinctTriangles([(7, 8, 9), (8, 7, 9), (7, 9, 8), (8, 9, 7), (9, 7, 8), (9, 8, 7)]))