// https://leetcode.com/problems/projection-area-of-3d-shapes

impl Solution {
    pub fn projection_area(grid: Vec<Vec<i32>>) -> i32 {
        let mut area_xy : i32 = 0;
        let mut area_xz : i32 = 0;
        let mut proj_yz : Vec<i32> = grid[0].clone();
        let n = grid.len();
        for i in 0..n {
            let m = grid[i].len();
            area_xz += grid[i].iter().max().unwrap();
            let w = proj_yz.len();
            for j in 0..m {
                let val = grid[i][j];
                if val > 0 {
                    area_xy += 1;
                }
                if j < w {
                    proj_yz[j] = proj_yz[j].max(val);
                } else {
                    proj_yz.push(val);
                }
            }
        }
        let area_yz : i32 = proj_yz.iter().sum();
        area_xy + area_xz + area_yz
    }
}