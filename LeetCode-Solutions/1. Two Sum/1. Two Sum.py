#
# Problem: 1. Two Sum
# Difficulty: Easy
# Link: https://leetcode.com/problems/two-sum/submissions/1954204788/
# Language: python3
# Date: 2026-03-20


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for every in range(0,len(nums)):
            remainder=target-nums[every]
            if remainder in seen:
                return [seen[remainder], every]
            else:
                seen[nums[every]]=every
