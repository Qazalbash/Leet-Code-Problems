// https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value

use std::collections::HashMap;

impl Solution {
    pub fn digit_count(num: String) -> bool {
        let mut count: HashMap<i32, i32> = HashMap::new();

        for i in num.chars() {
            *count.entry(i as i32 - 48).or_insert(0) += 1;
        }

        let n = num.len();
        let mut times : i32 = 0;
        for key in num.chars() {
            let value = *count.get(&times).unwrap_or(&0);
            if key as i32 != value + 48 {
                return false;
            }
            times += 1;
        }
        true
    }
}