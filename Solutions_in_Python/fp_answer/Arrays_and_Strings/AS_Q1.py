# Direct solution for Question 1. in Arrays and Strings
from typing import List


class Solution(object):
    
    def findClosestNumber(
        self,
        nums: List[int],
    ) -> int:
        """
        Given an integer array nums of size n, return the number with the value closest to 0 in nums.
        If there are multiple answers, return the number with the largest value.
        :type nums: List[int]
        :return results from Leetcode: Runtime: 101ms, beats 86.91%; Memory: 11.69 mb, beats 95.92%; 0(1)
        :rtype: int
        """
        if 0 in nums:
            return 0
        else:
            abs_nums = min([abs(x) for x in nums])
            if abs_nums in nums:
                return abs_nums
            else:
                return -abs_nums
