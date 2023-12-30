
def isAnagram( s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s)!= len(t):
        return False

    countS, countT= {}, {}
    for i in range(len(s)):
        countS[s[i]] = countS.get(s[i], 0) + 1
        countT[t[i]] = countT.get(t[i], 0) + 1
    
    for i in countS:
        if countS[i]!= countT[i]:
            return False
    
    return True
    
s ="himal"
t = "laih"
if (isAnagram(s,t)== True):
    print("True")
else:
    print("False")