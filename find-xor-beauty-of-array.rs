// https://leetcode.com/problems/find-xor-beauty-of-array

impl Solution {
    pub fn xor_beauty(nums: Vec<i32>) -> i32 {
        let mut xor : i32 = 0;
        let n : usize = nums.len();
        for i in 0..n {
            xor ^= nums[i];
        }
        (xor | xor) & xor
    }
}