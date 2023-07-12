// https://leetcode.com/problems/container-with-most-water

class Solution {
public:
    int maxArea(vector<int>& height) {
       int area = 0, n = height.size();
       int i = 0, j = n - 1;
       while(i < j) {
           if(height[i] > height[j]) {
               area = max(area, (j-i)*height[j]);
               --j;
           }
           else {
               area = max(area, (j-i)*height[i]);
               ++i;
           }
       }
       return area;
    }
};