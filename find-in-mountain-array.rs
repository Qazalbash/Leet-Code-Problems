// https://leetcode.com/problems/find-in-mountain-array

/**
 * // This is the MountainArray's API interface.
 * // You should not implement it, or speculate about its implementation
 *  struct MountainArray;
 *  impl MountainArray {
 *     fn get(index:i32)->i32;
 *     fn length()->i32;
 * };
 */

impl Solution {
    pub fn find_in_mountain_array(target: i32, mountainArr: &MountainArray) -> i32 {
        let mut left: i32 = 0;
        let mut right: i32 = mountainArr.length() - 1;
        let mut mid: i32 = 0;

        while left <= right {
            mid = (left + right) >> 1;

            let before = mountainArr.get(mid - 1);
            let at = mountainArr.get(mid);
            let after = mountainArr.get(mid + 1);

            let upward: bool = before < at && at < after;
            let downward: bool = before > at && at > after;

            if upward {
                left = mid + 1;
            } else if downward {
                right = mid;
            } else {
                break;
            }
        }

        let peak = mid;

        left = 0;
        right = mid;

        while left <= right {
            mid = (left + right) >> 1;
            let at = mountainArr.get(mid);
            if at == target {
                return mid;
            } else if at < target {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        left = peak;
        right = mountainArr.length() - 1;

        while left <= right {
            mid = (left + right) >> 1;
            let at = mountainArr.get(mid);
            if at == target {
                return mid;
            } else if at > target {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        -1
    }
}