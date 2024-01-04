// https://leetcode.com/problems/sum-multiples

impl Solution {
    pub fn sum_of_multiples(n: i32) -> i32 {
        if n < 3 {
            return 0;
        }
        let mut s : i32 = 0;
        for i in 3..=n {
            if i % 3 == 0 || i % 5 == 0 || i % 7 == 0 {
                s += i;
            }
        }
        s
    }
}