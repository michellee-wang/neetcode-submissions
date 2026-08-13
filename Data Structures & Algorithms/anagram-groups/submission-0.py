class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hsh = {}
        for i in range(len(strs)):
            if hsh != None:
                key = str(sorted(strs[i]))
                if key not in hsh:
                    hsh[key] = []
                hsh[key].append(strs[i])
        return list(hsh.values())
