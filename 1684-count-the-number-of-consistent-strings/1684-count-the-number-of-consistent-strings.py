class Solution(object):
    def countConsistentStrings(self, allowed, words):
        count = 0
        valid_set = set(allowed)

        for i in words:
                # if all(char in valid_set for char in i):
                # if set(i).issubset(valid_set):
                if set(i) <= valid_set:


                    count += 1
        return(count)
        