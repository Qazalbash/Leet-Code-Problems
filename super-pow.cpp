// https://leetcode.com/problems/super-pow

class Solution {
public:
    int superPow(int a, vector<int>& b) {
        if (a == 1) return a;
        
        const int n = b.size();
        int p = 1337;
        a %= p;
        int r = SM(a, b[0], p), ab;

        for(int i = 1; i < n; ++i) {
            r = SM(r, 10, p);
            ab = SM(a, b[i], p);
            r = (r * ab) % p;
        }
        return r;
    }

private:

    int SM(int a, int n, int p) {
        if (n == 0)
            return 1;
        if (n % 2)
            return (a * SM((a * a) % p, (n - 1) >> 1, p)) % p;
        else
            return SM((a * a) % p, n >> 1, p) % p;
    }
};