// https://leetcode.com/problems/search-in-rotated-sorted-array

impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        let mut left: usize = 0;
        let mut right: usize = nums.len() - 1;
        let mut mid: usize = 0;
        while left <= right {
            mid = (left + right) >> 1;
            if target == nums[mid] {
                return mid as i32;
            } 
            match nums[left] <= nums[mid] {
                true => match nums[left] <= target && target <= nums[mid] {
                        true => right = mid - 1,
                        false => left = mid + 1,
                    },
                false => match nums[mid] <= target && target <= nums[right] {
                        true => left = mid + 1,
                        false => right = mid - 1,
                    },
            }
        }
        -1
    }
}