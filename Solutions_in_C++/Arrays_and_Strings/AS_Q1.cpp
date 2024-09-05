//
// Created by Vickytoriah on 05 Sep 2024.
//
#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

class Solution {
public:
    /*
     * Given an integer array nums of size n, return the number with the value closest to 0 in nums.
        If there are multiple answers, return the number with the largest value.
        with NULL instead of null pointer: speed 2MS beats 98.67%;
        with nullptr, speed 10ms beats 94.75% & memory with 22.33 beats 90.15%.
    */
    int findClosestNumber (vector <int> &nums) {
        ios_base::sync_with_stdio (false);
        cin.tie(nullptr);
        int closest = nums[0];
        for (int num:nums) {
            if ((abs(num) < abs(closest)) || (num > closest && abs(num) == abs(closest))) {
                closest = num;
            }
        }
        return closest;
    }
};
