// https://leetcode.com/problems/h-index

impl Solution {
    pub fn h_index(mut citations: Vec<i32>) -> i32 {
        citations.sort();
        let n : usize = citations.len();

        if n == 1 && citations[0] == 0{
            return 0;
        }
        
        let mut h : i32 = 0;
        for i in 0..n {
            h = if citations[i] as usize + i < n {
                citations[i]
            } else {
                h.max((n-i) as i32)
            }
        }
        return h;
    }
}