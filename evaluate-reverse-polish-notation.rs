// https://leetcode.com/problems/evaluate-reverse-polish-notation

impl Solution {
    pub fn eval_rpn(tokens: Vec<String>) -> i32 {
        let mut stack: Vec<String> = Vec::new();
        for t in tokens {
            if t == "+" || t == "-" || t == "*" || t == "/" {
                let b: i32 = stack
                                .pop()
                                .unwrap()
                                .parse::<i32>()
                                .unwrap();
                let a: i32 = stack
                                .pop()
                                .unwrap()
                                .parse::<i32>()
                                .unwrap();
                stack.push(
                    {
                        if t == "+" { a + b }
                        else if t == "-" { a - b }
                        else if t == "*" { a * b }
                        else { a / b }
                    }.to_string()
                );
            } else {
                stack.push(t);
            }
        }
        stack
            .pop()
            .unwrap()
            .parse::<i32>()
            .unwrap()
    }
}