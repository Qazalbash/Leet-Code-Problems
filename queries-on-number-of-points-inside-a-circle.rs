// https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle

impl Solution {
    pub fn count_points(points: Vec<Vec<i32>>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let n_circles : usize = queries.len();
        let n_points : usize = points.len();
        let mut count : Vec<i32> = vec![0; n_circles];

        for i in 0..n_points {
            let x : i32 = points[i][0];
            let y : i32 = points[i][1];
            for j in 0..n_circles {
                let a : i32 = queries[j][0];
                let b : i32 = queries[j][1];
                let r : i32 = queries[j][2];
                if (x - a) * (x - a) + (y - b) * (y - b) <= r * r {
                    count[j] += 1;
                }
            }
        }
        return count;

    }
}