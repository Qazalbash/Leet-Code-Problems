// https://leetcode.com/problems/peak-index-in-a-mountain-array

impl Solution {
    pub fn peak_index_in_mountain_array(arr: Vec<i32>) -> i32 {
        let mut left = 0 as usize;
        let mut right = arr.len() - 1;
        let mut mid = 0 as usize;

        while left <= right {
            mid = (left + right) >> 1;

            if arr[mid - 1] < arr[mid] && arr[mid] < arr[mid + 1] {
                left = mid;
            } else if arr[mid - 1] > arr[mid] && arr[mid] > arr[mid + 1] {
                right = mid;
            } else {
                return mid as i32;
            }
        }
        mid as i32
    }
}