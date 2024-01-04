// https://leetcode.com/problems/check-if-the-sentence-is-pangram

impl Solution {
    pub fn check_if_pangram(sentence: String) -> bool {
        let mut p : u32 = 0 as u32;
        for s in sentence.chars() {
            p |= 1 << (s as u32 - 97 as u32);
        }
        p == 0x3FFFFFF
    }   
}