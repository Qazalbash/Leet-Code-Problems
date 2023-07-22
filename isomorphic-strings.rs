// https://leetcode.com/problems/isomorphic-strings

impl Solution {
    pub fn is_isomorphic(s: String, t: String) -> bool {
        return Solution::is_iso(&s, &t) && Solution::is_iso(&t, &s);
    }

    fn is_iso(s: &String, t: &String) -> bool {
        let mut mapping : std::collections::HashMap<usize, usize> = std::collections::HashMap::new();
        let vecs : Vec<char> = s.chars().collect();
        let vect : Vec<char> = t.chars().collect();
        let n : usize = s.len();
        for i in 0..n {
            let m : usize = (vecs[i] as usize) - (97 as usize);
            if mapping.contains_key(&m) == false {
                mapping.insert(m, (vect[i] as usize) - (96 as usize));
            } else if mapping[&m] != (vect[i] as usize) - (96 as usize) {
                return false;
            }
        }
        return true;
    }
}