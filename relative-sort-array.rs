// https://leetcode.com/problems/relative-sort-array

use std::collections::HashMap;

impl Solution {
    pub fn relative_sort_array(mut arr1: Vec<i32>, arr2: Vec<i32>) -> Vec<i32> {
    // Create a HashMap to store the indices of elements in arr2
    let mut arr2_indices: HashMap<i32, usize> = HashMap::new();
    for (index, &element) in arr2.iter().enumerate() {
        arr2_indices.insert(element, index);
    }

    // Sort arr1 based on the order of elements in arr2
    arr1.sort_by(|a, b| {
        let index_a = arr2_indices.get(a).unwrap_or(&usize::MAX);
        let index_b = arr2_indices.get(b).unwrap_or(&usize::MAX);
        index_a.cmp(index_b).then_with(|| a.cmp(b))
    });

    arr1
}
}