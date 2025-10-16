class Solution(object):
    def maxIncreasingSubarrays(self, nums):
        streak = []
        current_streak = [nums[0]]

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                current_streak.append(nums[i])
            else:
                streak.append(len(current_streak))
                current_streak = [nums[i]]

        streak.append(len(current_streak))

        minn = 0
        maxx = 1
        if len(streak) == 1:
            return streak[0]//2
        else:
            for i in range(len(streak)-1):
                if streak[i] >= streak[i+1]:
                    if streak[i]//2 >= min(streak[i] , streak[i+1]):
                        minn = streak[i]//2 
                    elif streak[i+1]//2 < min(streak[i] , streak[i+1]):
                        minn = min(streak[i] , streak[i+1])
                    else:
                        minn = min(streak[i] , streak[i+1])

                if streak[i] < streak[i+1]:
                    if streak[i]//2 >= min(streak[i] , streak[i+1]):
                        minn = streak[i]//2 
                    elif streak[i+1]//2 >= min(streak[i] , streak[i+1]):
                        minn = streak[i+1]//2 
                    else:
                        minn = min(streak[i] , streak[i+1])

                if minn >= maxx:
                    maxx = minn
            return(maxx)