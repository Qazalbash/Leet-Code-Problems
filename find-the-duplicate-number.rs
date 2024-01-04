// https://leetcode.com/problems/find-the-duplicate-number

impl Solution {
    pub fn find_duplicate(nums: Vec<i32>) -> i32 {
        let n: usize = nums.len() - 1;
        let m: usize = (n >> 6) + 1;
        let mut flag: Vec<usize> = vec![0 as usize; m];
        for i in nums {
            let s: usize = (i as usize) % 64;
            let k: usize = ((i as usize) - s) >> 6;
            let c: usize = (flag[k] & (0x1 << s)) >> s;
            if c == 1 {
                return i;
            }
            flag[k] |= 0x1 << s;
        }
        -1
    }
}