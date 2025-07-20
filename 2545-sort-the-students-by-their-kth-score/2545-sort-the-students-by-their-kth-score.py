class Solution(object):
    def sortTheStudents(self, score, k):
        for i in range(len(score)):
            for j in range(len(score) - 1):
                if score[j][k] < score[j + 1][k]:
                    score[j], score[j + 1] = score[j + 1], score[j] 

        return(score)

        