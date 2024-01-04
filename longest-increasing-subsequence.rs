// https://leetcode.com/problems/longest-increasing-subsequence

impl Solution {
    pub fn length_of_lis(nums: Vec<i32>) -> i32 {
        let n: usize = nums.len();
        let mut arr: Vec<i32> = vec![1; n];
        for i in 1..n {
            for j in 0..i {
                if nums[i] > nums[j] && arr[i] < arr[j] + 1 {
                    arr[i] = arr[j] + 1;
                }
            }
        }
        *arr.iter().max().unwrap()
    }
}