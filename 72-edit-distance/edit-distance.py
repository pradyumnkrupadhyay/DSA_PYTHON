class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if(len(word1) == 0 or len(word2) == 0):
            return max(len(word1),len(word2))
        
        
        matrix = []
        n = 0
        for i in range(0,len(word1)):
            tmp = list()
            for j in range(0,len(word2)):
                if(i == 0):
                    if(word1[i] == word2[j]):
                        if(j==0):
                            n+=0
                        else:
                            if(word1[i] in word2[0:j-1]):
                                n+=1
                            else:
                                n+=0
                    else:
                        n+=1
                    
                elif(i>0 and j == 0):
                    if(word1[i] == word2[j]):
                        if(word2[j] in word1[0:i-1]):
                            n = matrix[i-1][0] + 1
                        else:
                            n = matrix[i-1][0]
                    else:
                        n = matrix[i-1][0] + 1
                    
                else:
                    
                    if(word1[i] == word2[j]):
                        n = matrix[i-1][j-1]
                    else:
                        tri = min([tmp[j-1],matrix[i-1][j-1],matrix[i-1][j]])
                        n = tri+1

                tmp.append(n)
                
 
            matrix.append(tmp)


        return(matrix[i][j])