// https://leetcode.com/problems/fizz-buzz

impl Solution {
    pub fn fizz_buzz(n: i32) -> Vec<String> {
        let mut result : Vec<String> = Vec::new();
        for i in 1..=n {
            result.push(
                {
                    let div3 : bool = i % 3 == 0;
                    let div5 : bool = i % 5 == 0;
                    if div3 && div5 {
                        "FizzBuzz".to_string()
                    } else if div3 {
                        "Fizz".to_string()
                    } else if div5 {
                        "Buzz".to_string()
                    } else {
                        i.to_string()
                    }
                }
            );
        }
        return result;
    }
}