// https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation

use std::collections::HashMap;

impl Solution {
    pub fn count_prime_set_bits(mut left: i32, right: i32) -> i32 {
        let mut is_prime: HashMap<i32, bool> = HashMap::new();
        let mut count: i32 = 0;
        for i in left..=right {
            // println!("{:?}", is_prime);
            let bits = Solution::count_bits(i);
            if is_prime.contains_key(&bits) {
                if *is_prime.get(&bits).unwrap_or(&false) {
                    count += 1;
                }
                continue;
            }
            let prime = Solution::is_prime_number(bits);
            is_prime.insert(bits, prime);
            if prime {
                count += 1;
            }
        }
        count
    }

    fn count_bits(mut i: i32) -> i32 {
        let mut count: i32 = 0;
        while i != 0 {
            if i & 0x1 == 1 {
                count += 1;
            }
            i >>= 1;
        }
        count
    }

    fn is_prime_number(p: i32) -> bool {
        if p < 2 {
            return false;
        }
        if p % 2 == 0 {
            return p == 2;
        }
        let mut q: i32 = 3;
        while q * q <= p {
            if p % q == 0 {
                return false;
            }
            q += 2;
        }
        true
    }
}