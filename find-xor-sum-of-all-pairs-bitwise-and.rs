// https://leetcode.com/problems/find-xor-sum-of-all-pairs-bitwise-and

impl Solution {
    pub fn get_xor_sum(arr1: Vec<i32>, arr2: Vec<i32>) -> i32 {
        let n1: usize = arr1.len();
        let n2: usize = arr2.len();

        let mut a: i32 = arr1[0];

        for i in 1..n1 {
            a ^= arr1[i];
        }

        let mut b: i32 = arr2[0];

        for j in 1..n2 {
            b ^= arr2[j];
        }


        a & b
    }
}