'''
A bracket is any of the following characters: (, ), {, }, [, or ].
We consider two brackets to be matching if the first bracket is an open-bracket, 
e.g., (, {, or [, and the second bracket is a close-bracket of the same type. That means ( and ), [ and ], and { and } are the only pairs of matching brackets.
Furthermore, a sequence of brackets is said to be balanced if the following conditions are met:
The sequence is empty, or
The sequence is composed of two or more non-empty sequences, all of which are balanced, or
The first and last brackets of the sequence are matching, and the portion of the sequence without the first and last elements is balanced.
'''

def isBalanced(s):
  b_stack = []
  b_map = {'}':'{', ')':'(', ']':'['}
  for c in s:
    if c in b_map:
      if b_stack and b_stack[-1] == b_map[c]:
        b_stack.pop()
      else:
        return False
    else:
      b_stack.append(c)
  return False if len(b_stack) else True
  
print (isBalanced('{{[[(())]]}}'))
print (isBalanced('{}()[]'))
print (isBalanced('{[()]}'))
print (isBalanced('{(})'))
print (isBalanced('{('))