class Solution(object):
    def largestAltitude(self, gain):
        pre_fix =[0]*(len(gain)+1)

        for i in range(1,len(gain)+1):
            pre_fix[i]=pre_fix[i-1]+gain[i-1]
        return(max(pre_fix))
        