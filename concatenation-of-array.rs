// https://leetcode.com/problems/concatenation-of-array

impl Solution {
    pub fn get_concatenation(nums: Vec<i32>) -> Vec<i32> {
        let mut a : Vec<i32> = nums.iter().cloned().collect();
        let mut b : Vec<i32> = nums.iter().cloned().collect();
        a.extend(&b);
        a
    }
}