class Solution(object):
    def findPrefixScore(self, nums):
        ans = []
        max_so_far = float('-inf')
        score = 0

        for i in range(len(nums)):
            max_so_far = max(max_so_far, nums[i])  
            conver_value = nums[i] + max_so_far
            score += conver_value
            ans.append(score)

        return(ans)
        