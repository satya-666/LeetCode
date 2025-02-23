class Solution(object):
    def nextGreatestLetter(self, letters, target):
        n = len(letters)
        for i in range(n):
            if letters[i] > target:
                return letters[i]  
        return letters[0]

        