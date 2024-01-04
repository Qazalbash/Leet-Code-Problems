// https://leetcode.com/problems/utf-8-validation

impl Solution {
    pub fn valid_utf8(data: Vec<i32>) -> bool {
        let n: usize = data.len();
        let mut i: usize = 0;

        // println!("{:x?}", data);

        while i < n {
            let byte = data[i];
            let offset: usize = if byte & 0x80 == 0x0 {
                    0
                } else if byte & 0xe0 == 0xc0 {
                    1
                } else if byte & 0xf0 == 0xe0 {
                    2
                } else if byte & 0xf8 == 0xf0 {
                    3
                } else {
                    4
                };

            // println!("{}", offset);

            if offset == 4 {
                return false;
            } else if offset == 0 {
                i += 1;
                continue;
            }

            let mut j: usize = 1;

            while i + j < n && j <= offset {
                // println!("{:b}", data[i + j]);
                if data[i + j] & 0xc0 == 0x80 {
                    j += 1;
                } else {
                    return false;
                }
            }

            if j == offset + 1 {
                i += offset + 1;
            } else {
                return false;
            }
            // println!("{}", i);
        }
        true
    }
}