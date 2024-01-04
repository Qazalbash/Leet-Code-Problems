// https://leetcode.com/problems/number-of-digit-one

impl Solution {
    pub fn count_digit_one(N: i32) -> i32 {
        if N == 0 {
            return 0;
        }
        if N < 10 {
            return 1;
        }
        Solution::f(N as u32) as i32
    }

    fn f(n: u32) -> u32 {
        if n < 10 {
            if n == 0 {
                return 0;
            } else {
                return 1;
            }
        }
        
        let k: u32 = Solution::total_number_of_digits(n) - 1;
        let a: u32 = n / u32::pow(10, k);
        let b: u32 = n % u32::pow(10, k);
        
        if a == 1 {
            k * u32::pow(10, k - 1) + 1 + b + Solution::f(b)
        } else {
            (a * k + 10) * u32::pow(10, k - 1) + Solution::f(b)
        }
    }

    fn total_number_of_digits(mut N: u32) -> u32 {
        let mut n: u32 = 0 as u32;
        while (N != 0) {
            n += 1 as u32;
            N /= 10 as u32;
        }
        n
    }
}