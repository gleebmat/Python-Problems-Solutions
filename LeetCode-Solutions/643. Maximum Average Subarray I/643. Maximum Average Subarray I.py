#
# Problem: 643. Maximum Average Subarray I
# Difficulty: Easy
# Link: https://leetcode.com/problems/maximum-average-subarray-i/
# Language: python3
# Date: 2026-03-19


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_summary=summary=0
        summary=sum(nums[:k])
        max_summary=summary  
        for every in range(k, len(nums)):
            
            summary+=nums[every]-nums[every-k]
            if summary>max_summary:
                max_summary=summary
                
            
            
        return max_summary/k




