// https://leetcode.com/problems/count-largest-group

use std::collections::HashMap;

impl Solution {
    pub fn count_largest_group(n: i32) -> i32 {
        fn digit_sum(mut num: i32) -> i32 {
            let mut sum = 0;
            while num > 0 {
                sum += num % 10;
                num /= 10;
            }
            sum
        }

        let mut count: HashMap<i32, i32> = HashMap::new();

        for i in 1..=n {
            let sum = digit_sum(i);
            *count.entry(sum).or_insert(0) += 1;
        }

        let max_value = count.values().cloned().max().unwrap_or(0);
        count.values().filter(|&v| *v == max_value).count() as i32
    }
}