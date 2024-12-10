'''
Rotational Cipher
One simple way to encrypt a string is to "rotate" every alphanumeric character by a certain amount. 
Rotating a character means replacing it with another character that is a certain number of steps away in normal alphabetic or numerical order.
For example, if the string "Zebra-493?" is rotated 3 places, the resulting string is "Cheud-726?". 
Every alphabetic character is replaced with the character 3 letters higher (wrapping around from Z to A), and every numeric character replaced with the character 3 digits higher (wrapping around from 9 to 0). Note that the non-alphanumeric characters remain unchanged.
Given a string and a rotation factor, return an encrypted string.
'''
def rotationalCipher(input_str, rotation_factor):
  # Write your code here
  op_arr = []
  for c in input_str:
    val = ''
    if c >= 'a' and c <= 'z':
      val = chr((ord(c) - ord('a') + rotation_factor) % 26 + ord('a'))
    elif c >= 'A' and c <= 'Z':
      val = chr((ord(c) - ord('A') + rotation_factor) % 26  + ord('A'))
    elif c >= '0' and c <= '9':
      val = chr((ord(c) - ord('0') + rotation_factor) % 10 + ord('0'))
    else:
      val = c
    op_arr.append(val)
  return ''.join(op_arr)

print (rotationalCipher("All-convoYs-9-be:Alert1.", 4))
print (rotationalCipher("abcdZXYzxy-999.@", 200))