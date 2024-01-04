// https://leetcode.com/problems/third-maximum-number

impl Solution {
    pub fn third_max(nums: Vec<i32>) -> i32 {
        if nums.len() < 3 as usize {
            return *nums.iter().max().unwrap();
        }
        
        let mut a : i64 = std::i64::MIN;
        let mut b : i64 = std::i64::MIN;
        let mut c : i64 = std::i64::MIN;

        for n in nums {
            let n64 : i64 = n as i64;
            if n64 == a || n64 == b || n64 == c {
                continue;
            } else if n64 > a {
                c = b;
                b = a;
                a = n64;
            } else if n64 > b {
                c = b;
                b = n64;
            } else if n64 > c {
                c = n64;
            }
        }
        if c == std::i64::MIN {
            a as i32
        } else {
            c as i32
        } 
    }
}