// https://leetcode.com/problems/find-smallest-letter-greater-than-target

class Solution {
public:
    char nextGreatestLetter(vector<char>& letters, char target) {
        const int n = letters.size();
        if (target >= letters[n-1]) return letters[0];
        int mid, left = 0, right = n - 1;
        while (left <= right) {
            mid = ( left + right ) >> 1;
            if (letters[mid] <= target) left = mid + 1;
            else                       right = mid - 1;
        }
        if (left < 0) return letters[0];
        else if (left >= n) return letters[n-1];
        return letters[left];
    }
};