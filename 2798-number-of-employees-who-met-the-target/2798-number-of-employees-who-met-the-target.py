class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        arr = []
        for i in hours:
            if i >= target:
                arr.append(i)
        return(len(arr))
        