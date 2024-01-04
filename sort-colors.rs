// https://leetcode.com/problems/sort-colors

impl Solution {
    pub fn sort_colors(nums: &mut Vec<i32>) {
        let mut zero = 0;
        let mut one = 0;
        let mut two = 0;


        for i in nums.into_iter() {
            if *i == 0 {
                zero += 1;
            } else if *i == 1 {
                one += 1;
            } else {
                two += 1;
            }
        }

        let mut index : usize = 0 as usize;

        while zero > 0 {
            nums[index] = 0;
            zero -= 1;
            index += 1;
        }

        while one > 0 {
            nums[index] = 1;
            one -= 1;
            index += 1;
        }

        while two > 0 {
            nums[index] = 2;
            two -= 1;
            index += 1;
        }
    }
}