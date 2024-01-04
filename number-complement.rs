// https://leetcode.com/problems/number-complement

impl Solution {
    pub fn find_complement(mut num: i32) -> i32 {
        let mut r: i32 = 0;
        let mut i: i32 = 0;
        while num > 0 {
            r |= (!num & 0x1) << i;
            num >>= 1;
            i += 1;
        }
        r
    }
}