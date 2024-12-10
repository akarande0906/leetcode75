


from functools import cache

def canGetExactChange(targetMoney, denominations):
    if targetMoney == 0:
        return True
    if targetMoney < 0:
        return False
    for d in denominations:
        if canGetExactChange(targetMoney - d, denominations):
            return True
    return False


print(canGetExactChange(94, [5, 10, 25, 100, 200]))
print(canGetExactChange(95, [5, 10, 25, 100, 200]))
print(canGetExactChange(75, [4, 17, 29]))