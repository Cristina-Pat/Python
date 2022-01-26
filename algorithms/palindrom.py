
from re import X


class Palindrome: 
    def __init__ (self, aWord):
        self.word = aWord 

    def isPalindrome(x):
        if len(x) == 0 or len(x) == 1:
            result = True
        if x[0] == x[len-1]:
            result = isPalindrome(x[1, len-1])
        result = False
        print(result)




