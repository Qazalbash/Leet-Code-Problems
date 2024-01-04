// https://leetcode.com/problems/kth-largest-element-in-an-array

impl Solution {
    pub fn find_kth_largest(mut nums: Vec<i32>, mut k: i32) -> i32 {
        // let mut set: Vec<i32> = vec![nums[0]];

        nums.sort();
        // println!("{:?}", nums);
        let n: usize = nums.len();
        nums[n - (k as usize)]
    }

    // fn seach(arr: &Vec<i32>, target: i32) -> (bool, usize) {
    //     let mut left: usize = 0;
    //     let mut right: usize = arr.len() - 1;
    //     let mut mid: usize = 0;
    //     while left <= right {
    //         mid = (left + right) >> 1;
    //         if arr[mid] == target {
    //             return (true, mid);
    //         } else if arr[mid] < target {
    //             right = mid - 1;
    //         } else {
    //             left = mid + 1;
    //         }
    //     }
    //     (false, left)
    // }
}