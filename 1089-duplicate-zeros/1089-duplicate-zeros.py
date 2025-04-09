class Solution(object):
    def duplicateZeros(self, arr):
        i ,j = 0,len(arr)-1

        while (i<j):
            if arr[i]==0:
                arr.insert(i+1,0)
                arr.pop()
                i+=2
            else:
                i+=1

        return(arr)
                