class Solution(object):
    def findSpecialInteger(self, arr):
        part = len(arr)//4
        arr_dict = {}

        for i in arr:
            if i in arr_dict:
                arr_dict[i] += 1
            else:
                arr_dict[i] = 1
        for keys,value in arr_dict.items():
            if value > part:
                return keys
        return None