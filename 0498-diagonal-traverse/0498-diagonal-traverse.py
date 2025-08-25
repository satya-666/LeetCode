class Solution(object):
    def findDiagonalOrder(self, mat):
        m = len(mat)
        n = len(mat[0])
        ans = []
        mat_dict= {}
        for i in range(m):
            for j in range(n):
                d = i+j
                if d not in mat_dict:
                    mat_dict[d] = []
                mat_dict[d].append(mat[i][j])


        for keys ,vales in mat_dict.items():
            if keys%2 == 0:
                ans.extend(vales[::-1])
            else:
                ans.extend(vales)

        return(ans)