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
        :rtype: int
        """
        abs_nums_list = [abs(x) for x in nums]
        closest_num = min(abs_nums_list)
        if closest_num in nums:
            return closest_num
        else:
            return -closest_num
    
    
    def findClosestNumber_faster(
        self,
        nums: List[int],
    ) -> int:
        """
        Given an integer array nums of size n, return the number with the value closest to 0 in nums.
        If there are multiple answers, return the number with the largest value.
        :type nums: List[int]
        :rtype: int
        """
        if 0 in nums:
            return 0
        else:
            closest_num = 1
            for num in nums:
                if abs(num)
            
        abs_nums_list = [abs(x) for x in nums]
        closest_num = min(abs_nums_list)
        if closest_num in nums:
            return closest_num
        else:
            return -closest_num