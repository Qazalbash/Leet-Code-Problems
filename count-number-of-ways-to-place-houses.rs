// https://leetcode.com/problems/count-number-of-ways-to-place-houses

impl Solution {
    pub fn count_house_placements(mut n: i32) -> i32 {
        let mut a : usize = 1;
        let mut b : usize = 1;
        let mut c : usize = 0;
        let p : usize = 10_usize.pow(9) + 7;

        while n > 0 {
            c = ((a % p) + (b % p)) % p;
            a = b % p;
            b = c;
            n -= 1;
        }
        return (((c % p) * (c % p)) % p) as i32;
    }
}