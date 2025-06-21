class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        ransomNote = list(ransomNote)
        magazine = list(magazine)

        result = 0

        if len(ransomNote) > len(magazine):
            return(False)
        else:
            for i in ransomNote:
                if i in magazine:
                    magazine.remove(i)
                    result += 1
                else:
                    return(False)
                    break

            if result == len(ransomNote):
                return(True)
        