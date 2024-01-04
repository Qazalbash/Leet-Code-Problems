// https://leetcode.com/problems/find-triangular-sum-of-an-array

impl Solution {
    pub fn triangular_sum(mut nums: Vec<i32>) -> i32 {
        let n = nums.len();
        for level in 1..n {
            for j in 0..(n-level) {
                nums[j] = (nums[j] + nums[j+1]) % 10;
            }
        }
        nums[0]
    }
}