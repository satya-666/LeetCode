class Solution(object):
    def minOperations(self, boxes):
        n = len(boxes)
        answer = [0] * n

        steps = 0
        ball_count = 0
        for i in range(n):
            answer[i] += steps
            if boxes[i] == '1':
                ball_count += 1
            steps += ball_count

        steps = 0
        ball_count = 0
        for i in range(n - 1, -1, -1):
            answer[i] += steps
            if boxes[i] == '1':
                ball_count += 1
            steps += ball_count

        return(answer)