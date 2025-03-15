class Solution(object):
    def kthGrammar(self, n, k):
        if n == 1:  
            return 0  

        length_of_prev_row = 2**(n - 2)  

        if k <= length_of_prev_row:  
            return self.kthGrammar(n - 1, k)  
        else:  
            return 1 - self.kthGrammar(n - 1, k - length_of_prev_row)