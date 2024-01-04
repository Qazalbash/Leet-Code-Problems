// https://leetcode.com/problems/set-mismatch

impl Solution {
    pub fn find_error_nums(mut nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let mut result = vec![];

        let mut seen = std::collections::HashSet::new();
        let mut duplicate = 0;
        for num in &nums {
            if !seen.insert(*num) {
                duplicate = *num;
                break;
            }
        }

        let expected_sum = ( n * n + n ) >> 1;
        let actual_sum : i32 = nums.iter().sum();
        let missing = expected_sum as i32 - actual_sum + duplicate;

        result.push(duplicate);
        result.push(missing);

        result
    }
}