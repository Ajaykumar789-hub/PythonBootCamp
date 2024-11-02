## Order should be maintained and they can be non continuous

def subseq(s):
    if s == '':
        ans= ['']
        return ans
    smallAns = subseq(s[1:]) ##[b,c,'']
    mychar = s[0]
    ans = []
    ans.extend(smallAns) ##[b,c,bc,'']

    for perm in smallAns:
        ans.append(mychar + perm)
    return ans

print(subseq("ajay"))
    
    