#
# Problem: 3. Longest Substring Without Repeating Characters
# Difficulty: Medium
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/1954235957/
# Language: python3
# Date: 2026-03-20


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maximum=0
        count=0
        left,right=0,0
        unique={}
        for right in range(len(s)):
            if s[right] in unique and unique[s[right]]>=left:
                left=unique[s[right]]+1
            
            
            unique[s[right]]=right
            count=right-left+1
            if count>maximum:
                    maximum=count
        return maximum
            
