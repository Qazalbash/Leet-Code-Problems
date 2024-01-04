// https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array

impl Solution {
    pub fn difference_of_sum(nums: Vec<i32>) -> i32 {
        let mut diff: i32 = 0;
        for i in nums {
            diff += i - Solution::ds(i);
        }
        diff.abs()
    }

    fn ds(mut n: i32) -> i32 {
        let mut s: i32 = 0;
        while n > 0 {
            s += n % 10;
            n /= 10;
        }
        s
    }
}