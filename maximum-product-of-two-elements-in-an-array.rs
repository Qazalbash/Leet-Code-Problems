// https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array

impl Solution {
    pub fn max_product(mut nums: Vec<i32>) -> i32 {
        nums.sort();
        let n = nums.len();
        (nums[n-1] - 1) * (nums[n-2] - 1)
    }
}