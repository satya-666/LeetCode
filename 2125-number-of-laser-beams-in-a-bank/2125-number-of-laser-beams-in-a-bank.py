class Solution(object):
    def numberOfBeams(self, bank):
        leaser = 0
        arr = [0] * len(bank)

        for i in range(len(bank)):
            arr[i] = bank[i].count("1")


        prev = 0
        for i in range(len(arr)):
            if arr[i] != 0:
                leaser += prev * arr[i]
                prev = arr[i]

        return(leaser)