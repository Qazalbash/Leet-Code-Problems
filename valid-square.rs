// https://leetcode.com/problems/valid-square

impl Solution {
    pub fn valid_square(p1: Vec<i32>, p2: Vec<i32>, p3: Vec<i32>, p4: Vec<i32>) -> bool {
        let lengths: Vec<i32> = vec![
            Solution::dist_sq(&p1, &p2),
            Solution::dist_sq(&p1, &p3),
            Solution::dist_sq(&p1, &p4),
            Solution::dist_sq(&p3, &p4),
            Solution::dist_sq(&p2, &p3),
            Solution::dist_sq(&p2, &p4),
        ];


        let side: i32 = *lengths.iter().min().unwrap();
        let diag: i32 = *lengths.iter().max().unwrap();

        (side << 1 == diag) && side != 0
    }


    fn dist_sq(p1: &Vec<i32>, p2: &Vec<i32>) -> i32 {
        let x1 = p1[0];
        let y1 = p1[1];

        let x2 = p2[0];
        let y2 = p2[1];

        (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
    }
}