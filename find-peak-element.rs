// https://leetcode.com/problems/find-peak-element

impl Solution {
    pub fn find_peak_element(nums: Vec<i32>) -> i32 {
        let n: usize = nums.len();
        let mut index: usize = 0;
        for i in 0..n {
            if nums[i] > nums[index] {
                index = i;
            }
        }
        index as i32
        // let mut left: usize = 0;
        // let mut right: usize = nums.len() - 1;
        // if right == 0 {
        //     return 0;
        // }
        // let mut mid: usize = 0;

        // while left <= right {
        //     mid = (left + right) >> 1;

        //     if mid == 0 {
        //         return if nums[mid] > nums[mid + 1] {
        //             mid as i32
        //         } else {
        //             (mid + 1) as i32
        //         };
        //     } else if mid == n - 1 {
        //         return if nums[mid - 1] < nums[mid] {
        //             mid as i32
        //         } else {
        //             (mid - 1) as i32
        //         };
        //     }
        //     else if nums[mid - 1] < nums[mid] && nums[mid] < nums[mid + 1] {
        //         left = mid + 1;
        //     } else if nums[mid - 1] > nums[mid] && nums[mid] > nums[mid + 1] {
        //         right = mid;
        //     } else {
        //         return mid as i32;
        //     }
        // }
        // mid as i32
    }
}