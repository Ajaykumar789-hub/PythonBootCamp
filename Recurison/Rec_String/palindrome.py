
s = 'nitiN'
s2 = "Ajaykumar"

def palindrome_helper(s,start, end):
    if start>=end:
        return True
    if s[start] != s[end]:
        return False
    return palindrome_helper(s, start+1, end-1)

def palindrome(s):
    s = s.lower()
    return palindrome_helper(s,0, len(s)-1)

print(palindrome(s))
print(palindrome(s2))
    