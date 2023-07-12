// https://leetcode.com/problems/guess-number-higher-or-lower

/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

class Solution {
public:
    int guessNumber(int n) {
        size_t i = 1, j = n, k;
        while (i <= j) {
            k = (i + j) >> 1;
            const int g = guess(k);
            if (g == -1) {
                j = k - 1;
            } else if (g == 1) {
                i = k + 1;
            } else {
                return k;
            }
        }
        return k;
    }
};