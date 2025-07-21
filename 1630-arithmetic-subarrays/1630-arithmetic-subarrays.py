class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        result = []
        i,j = 0,0
        while i < len(r) and j < len(r):
            num = nums[l[i]:r[j]+1]
            i += 1
            j += 1
            num.sort()
            diff = num[1]-num[0]
            count = 0
            result_counter = 0
            for k in range(len(num)-1):
                if num[k+1]-num[k] != diff:
                    count += 1
            if count == 0:
                result.append(True)
            else:
                result.append(False)
        return(result)
        