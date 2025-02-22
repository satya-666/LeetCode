class Solution(object):
    def flipAndInvertImage(self, image):
        for i in range(len(image)):
            k = len(image[i]) - 1
            for j in range(len(image[i])//2):
                image[i][j], image[i][k - j] = image[i][k - j], image[i][j]
            for j in range(k+1):
                if image[i][j]==0:
                    image[i][j]=1
                else:
                    image[i][j]=0

        return(image)