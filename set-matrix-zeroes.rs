// https://leetcode.com/problems/set-matrix-zeroes

impl Solution {
    pub fn set_zeroes(matrix: &mut Vec<Vec<i32>>) {
        let mut row_index : Vec<usize> = Vec::new();
        let mut col_index : Vec<usize> = Vec::new();
        let m : usize = matrix.len();
        let n : usize = matrix[0].len();

        for i in 0..m {
            for j in 0..n {
                if matrix[i][j] == 0 {
                    row_index.push(i);
                    col_index.push(j);
                }
            }
        }

        for r in &row_index {
            for j in 0..n {
                matrix[*r][j] = 0;
            }
        }
        
        for i in 0..m {
            for c in &col_index {
                matrix[i][*c] = 0;
            }
        }
    }
}