// https://leetcode.com/problems/number-of-common-factors

impl Solution {
    pub fn common_factors(a: i32, b: i32) -> i32 {
        let mut gcd = Solution::gcd(a, b);
        let mut count: i32 = 1;
        let mut p: i32 = 2;
        while p <= gcd && gcd != 0 {
            let mut i: i32 = 0;
            while gcd % p == 0 {
                i += 1;
                gcd /= p;
            }
            p += 1;
            count *= i + 1;
        }
        count
    }

    fn gcd(mut a: i32, mut b: i32) -> i32 {
        while b != 0{
            let t = b;
            b = a % b;
            a = t;
        }
        a
    }
}