// https://leetcode.com/problems/maximum-number-of-groups-entering-a-competition

class Solution {
public:
    int maximumGroups(vector<int>& grades) {
        // sort(grades.begin(), grades.end());
        /*
        total * total + total - 2 * n = 0
    =>  2 * total = (-1 + sqrt(1 + 8 * n)) / 2
        */ 
        
        int total = grades[0];
        const int n = grades.size();
        const int d = sqrt(1 + (n << 3));
        return ((d-1) >> 1);
        // for (int i = )
    }
};