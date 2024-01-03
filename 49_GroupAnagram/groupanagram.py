strs = ["eat","tea","tan","ate","nat","bat"]

def groupAnagrams(strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        check = {}
        for strings in strs:
            sortedString = ''.join(sorted(strings))
            if sortedString in check:
                check[sortedString].append(strings)
            else:
                check[sortedString] = [strings]   
        return list(check.values())
    

print(groupAnagrams(strs))