// https://leetcode.com/problems/rotate-function

impl Solution {
    pub fn max_rotate_function(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut F: Vec<i32> = vec![0; n];
        let mut S: i32 = 0;
        for i in 0..n {
            F[0] += (i as i32) * nums[i];
            S += nums[i];
        }
        let mut ans: i32 = F[0];
        for i in 1..n {
            F[i] = F[i-1] + S - (n as i32) * nums[n-i];
            ans = ans.max(F[i]);
        }
        ans
    }
}