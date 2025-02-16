class Solution(object):
    def twoSum(self, numbers, target):
        i,j = 0,len(numbers)-1
        while j <len(numbers):
            if numbers[i]+numbers[j]==target:
                return([i+1,j+1])
                break
            elif numbers[i]+numbers[j]<target:
                i+=1
            else:
                j -=1
            

        