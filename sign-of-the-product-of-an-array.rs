// https://leetcode.com/problems/sign-of-the-product-of-an-array

impl Solution {
    pub fn array_sign(nums: Vec<i32>) -> i32 {
        let mut sign: bool = true;
        for x in nums {
            if x == 0 {
                return 0;
            } else if x < 0 {
                sign = !sign;
            }
        }
        match sign {
            true => 1,
            false => -1,
        }
    }
}