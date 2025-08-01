class Solution(object):
    def countStudents(self, students, sandwiches):
        zero_cnt = 0
        one_cnt = 0

        for i in students:
            if i == 0:
                zero_cnt += 1
            else:
                one_cnt += 1
        for j in sandwiches:
            if j == 0:
                if zero_cnt == 0:
                    break
                zero_cnt -= 1
            else:
                if one_cnt == 0:
                    break
                one_cnt -= 1
        return (zero_cnt + one_cnt)

        