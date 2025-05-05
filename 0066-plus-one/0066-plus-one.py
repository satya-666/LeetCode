class Solution(object):
    def plusOne(self, digits):
        power = 10**(len(digits)-1)

        total = 0
        for i in digits:
            total+=i*power
            power=power//10

        result = str(total+1)


        sum_digit = []
        for i in range(len(result)):
            sum_digit.append(int(result[i]))

        return(sum_digit)



        