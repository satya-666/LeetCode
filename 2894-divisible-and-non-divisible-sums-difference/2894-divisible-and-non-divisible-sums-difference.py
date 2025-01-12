class Solution(object):
    def differenceOfSums(self, n, m):
        num1 = []
        num2 = []
        for i in range(1,n+1):
            if i % m != 0:
                num1.append(i)
            if i % m ==0:
                num2.append(i)

        kim = sum(num1)
        sim = sum(num2)

        return(kim-sim)
        