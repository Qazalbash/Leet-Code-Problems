// https://leetcode.com/problems/bitwise-xor-of-all-pairings

impl Solution {
    pub fn xor_all_nums(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let n1: usize = nums1.len();
        let n2: usize = nums2.len();
        
        let mut xor: i32 = 0;

        if n2 % 2 == 1 {
            for i in 0..n1 {
                xor ^= nums1[i];
            }
        }

        if n1 % 2 == 1 {
            for i in 0..n2 {
                xor ^= nums2[i];
            }
        }
        
        xor
    }
}