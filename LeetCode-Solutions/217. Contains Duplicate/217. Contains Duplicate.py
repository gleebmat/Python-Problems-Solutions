#
# Problem: 217. Contains Duplicate
# Difficulty: Easy
# Link: https://leetcode.com/problems/contains-duplicate/description/
# Language: python3
# Date: 2026-03-19


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums))<len(nums)

