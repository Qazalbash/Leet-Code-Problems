// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        for(int i=0;i<size(numbers);i++){
            for(int j=i+1;j<size(numbers);j++){
                if(numbers[i]+numbers[j]==target){
                    return {i+1,j+1};
                }
            }
        }
    return {0,0};
    }
};