class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return("")
        else:
            k = len(min(strs, key=len))
            arr = []
            for i in range(k):
                if all(word[i] == strs[0][i] for word in strs):
                    arr.append(strs[0][i])
                else:
                    break
            return("".join(arr))
        
