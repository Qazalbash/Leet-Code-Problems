// https://leetcode.com/problems/maximum-subarray

impl Solution {
    pub fn max_sub_array(mut nums: Vec<i32>) -> i32 {
        let mut current: i32 = 0;
        let mut best: i32 = 0;
        for n in &nums {
            current = std::cmp::max(0, current + *n);
            best = std::cmp::max(best, current);
        }
        if best == 0 {
            *nums.iter().max().unwrap()
        } else {
            best
        }
    }
}