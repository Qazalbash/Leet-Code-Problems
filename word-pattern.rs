// https://leetcode.com/problems/word-pattern

impl Solution {
    pub fn word_pattern(pattern: String, s: String) -> bool {
        let mut s_map_t : std::collections::HashMap<&str, char> = std::collections::HashMap::new();
        let mut t_map_s : std::collections::HashMap<char, &str> = std::collections::HashMap::new();
        let vecs : Vec<&str> = s.split_whitespace().collect();
        let vect : Vec<char> = pattern.chars().collect();
        let n : usize = vecs.len();
        let m : usize = vect.len();

        if m != n { return false; }

        for i in 0..n {
            let s_to_t : &str = &vecs[i];
            let t_to_s : char = vect[i];
            let image_of_s : char = t_to_s;
            let image_of_t : &str = s_to_t;

            if s_map_t.contains_key(&s_to_t) == false {
                s_map_t.insert(s_to_t, image_of_s);
            } else if s_map_t[&s_to_t] != image_of_s {
                return false;
            }

            if t_map_s.contains_key(&t_to_s) == false {
                t_map_s.insert(t_to_s, image_of_t);
            } else if t_map_s[&t_to_s] != image_of_t {
                return false;
            }
        }
        return true;
    }
}