def isPalindrome(x):
    if len(x) == 0 or len(x) == 1:
        return True
    elif x[0] == x[len(x)-1]:
        return isPalindrome(x[1:len(x)-1])
    return False



print(isPalindrome('beca'))
print(isPalindrome('racecar'))