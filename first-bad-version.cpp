// https://leetcode.com/problems/first-bad-version

// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        long left = 1;
        long right = n;
        long mid;
        bool isBad;
        while (left <= right) {
            mid = (left + right) >> 1;
            isBad = isBadVersion(mid);
            if (isBad) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
};