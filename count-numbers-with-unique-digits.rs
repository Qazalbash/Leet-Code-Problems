// https://leetcode.com/problems/count-numbers-with-unique-digits

impl Solution {
    pub fn count_numbers_with_unique_digits(n: i32) -> i32 {
        let mut fact: [i32; 10] = [1; 10];
        for i in 0..9 {
            fact[i+1] = ((i+1) as i32) * fact[i];
        }
        let mut total: i32 = 1;

        for k in 1..=n {
            total += 9 * fact[9] / fact[(10-k) as usize];
        }

        total
    }
}