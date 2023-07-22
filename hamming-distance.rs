// https://leetcode.com/problems/hamming-distance

impl Solution {
    pub fn hamming_distance(x: i32, y: i32) -> i32 {
        let mut xy = x ^ y;
        let mut count = 0;
        while xy > 0 {
            if xy & 1 == 1 {
                count += 1;
            }
            xy >>= 1;
        }
        return count;
    }
}