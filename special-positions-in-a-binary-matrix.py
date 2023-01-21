// https://leetcode.com/problems/special-positions-in-a-binary-matrix

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        cor=0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==1 and sum(mat[i])==1:
                    p=0
                    for k in range(len(mat)):
                        p+=mat[k][j]==1
                    if p==1:
                        cor+=1
                        
                        
        return cor