def isomorphic(s, t):
    if len(s) != len(t):
        return False
    mapST, mapTS = {}, {}
    for charS, charT in zip(s, t):
        # If isomorphic both side mapping should hold good
        if (charS in mapST and mapST[charS] != charT) or (charT in mapTS and mapTS[charT] != charS):
            return False
        mapST[charS] = charT
        mapTS[charT] = charS
    return True

print(isomorphic('cbcrt', 'abaxv'))
print(isomorphic('abb', 'cdd'))
print(isomorphic('abcd', 'bbcd'))
print(isomorphic('abcd', 'bxcd'))
