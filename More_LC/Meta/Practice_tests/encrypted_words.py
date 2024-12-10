

def findEncryptedWord(s):
  # Write your code here
  
  def encrypt(s, left, right):
    if len(s) == 1:
      return s
    if left > right:
      return ''
    mid =  (left + right) // 2
    return s[mid] + encrypt(s, left, mid-1) + encrypt(s, mid+1, right)
    
  return encrypt(s, 0, len(s) - 1)


print (findEncryptedWord('abcxcba'))
print (findEncryptedWord('facebook'))
print (findEncryptedWord('abc'))
print (findEncryptedWord('abcd'))
print (findEncryptedWord('abcdefghijkl'))
