// https://leetcode.com/problems/first-unique-character-in-a-string

impl Solution {
    pub fn first_uniq_char(s: String) -> i32 {
        let n: usize = s.len();
        let mut repeat: [bool; 26] = [false; 26];
        let mut index: [usize; 26] = [std::usize::MAX; 26];

        let mut k: usize = 0;
        for c in s.chars() {
            let i: usize = (c as usize) % 26;
            if repeat[i] {
                index[i] = std::usize::MAX;
            } else {
                index[i] = k;
                repeat[i] = true;
            }
            k += 1;
        }
        
        let mut ans: usize = std::usize::MAX;
        for i in 0..26 {
            ans = std::cmp::min(ans, index[i]);
        }
        
        match ans == std::usize::MAX {
            true => -1,
            false => ans as i32,
        }
    }
}