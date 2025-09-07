'''
Objective: Given a number, find out whether it is colorful.

Colorful Number: When in a given number, the product of every contiguous sub-sequence is different. 
That number is called a Colorful Number. 
E.g.: Number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245.
this number is a colorful number, since product of every digit of a sub-sequence are different.
That is, 3 2 4 5 (3*2)=6 (2*4)=8 (4*5)=20, (3*2*4)= 24 (2*4*5)= 40
'''

def isColorful(number):
    colorString = str(number)
    length = len(colorString)
    product_seen = set()
    for i in range(length):
        product = 1
        for j in range(i, length):
            product *= int(colorString[j])
            if product in product_seen:
                return False
            else:
                product_seen.add(product)
    return True

print (isColorful(326))
print (isColorful(3245))
