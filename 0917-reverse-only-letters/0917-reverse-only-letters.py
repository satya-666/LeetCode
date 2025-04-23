class Solution(object):
    def reverseOnlyLetters(self, s):
        alpha_arr = list(s)
        i, j = 0, len(alpha_arr) - 1

        while i < j:
            if alpha_arr[i].isalpha() and alpha_arr[j].isalpha():
                alpha_arr[i], alpha_arr[j] = alpha_arr[j], alpha_arr[i]
                i += 1
                j -= 1
            elif not alpha_arr[i].isalpha():
                i += 1
            elif not alpha_arr[j].isalpha():
                j -= 1

        return("".join(alpha_arr))