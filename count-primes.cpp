// https://leetcode.com/problems/count-primes

class Solution {
public:
    int countPrimes(int n) {
        if (n < 2) return n == 2;
        int p[n];
        for(int i = 0; i < n; ++i) p[i] = 1;
        int prime = 2, count = 0;
        while (prime < n) {
            for(int i = prime + prime; i < n; i += prime) p[i] = 0;
            do { ++prime; } while(prime < n && p[prime] == 0);
            ++count;
        }
        return count;
    }
};