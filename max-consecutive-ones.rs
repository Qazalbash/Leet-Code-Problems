// https://leetcode.com/problems/max-consecutive-ones

impl Solution {
    pub fn find_max_consecutive_ones(nums: Vec<i32>) -> i32 {
        let mut max_so_far : i32 = 0;
        let mut count : i32 = 0;
        for n in nums {
            if n == 1 {
                count += 1;
            } else {
                max_so_far = max_so_far.max(count);
                count = 0;
            }
        }
        return max_so_far.max(count);
    }
}