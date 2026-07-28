#
# Problem: 48. Rotate Image
# Difficulty: Medium
# Link: https://leetcode.com/problems/rotate-image/
# Language: python3
# Date: 2026-03-19


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        length=len(matrix)
        for i in range(0, length):
            for j in range(i, length):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for every in range(0,length):
            matrix[every].reverse()
        
