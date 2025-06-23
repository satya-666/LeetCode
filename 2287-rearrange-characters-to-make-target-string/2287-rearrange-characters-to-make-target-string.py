class Solution(object):
    def rearrangeCharacters(self, s, target):
        if len(s) < len(target):
            return 0

        s_dict = {}
        target_dict = {}

        for char in target:
            if char in target_dict:
                target_dict[char] += 1
            else:
                target_dict[char] = 1

        for char in s:
            if char in s_dict:
                s_dict[char] += 1
            else:
                s_dict[char] = 1

        min_repeats = float('inf')
        for char in target_dict:
            if char not in s_dict:
                return 0
            min_repeats = min(min_repeats, s_dict[char] // target_dict[char])

        return min_repeats

