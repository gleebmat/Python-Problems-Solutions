#
# Problem: 11. Container With Most Water
# Difficulty: Medium
# Link: https://leetcode.com/problems/container-with-most-water/
# Language: python3
# Date: 2026-03-21


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        areaNow=0
        right=len(height)-1
        maxArea=(right-left)*min(height[left],height[right])

        while left<right:
            areaNow=(right-left)*min(height[left],height[right])
            if areaNow>maxArea:
                maxArea=areaNow
            if height[left]>height[right]:
                right-=1
            else:
                left+=1
        return maxArea

