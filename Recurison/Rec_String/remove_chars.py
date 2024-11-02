s = "ajayzz"
c = "z"
def remove_char(s,c):
    if len(s) == 0 or s =='':
        return s
    smallans = remove_char(s[1:],c)

    if s[0]==c:
        return smallans
    else:
        return s[0] + smallans
    
print(remove_char(s,c))