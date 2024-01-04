// https://leetcode.com/problems/alternating-digit-sum

impl Solution {
    pub fn alternate_digit_sum(mut n: i32) -> i32 {
        let mut sum: i32 = 0;
        let mut sign: i32 = 1;
        let mut i = 0;
        while n != 0 {
            i += 1;
            sum += sign * (n % 10);
            n /= 10;
            sign *= -1;
        }
        if i % 2 == 0 {
            sum *= -1;
        }
        sum
    }
}