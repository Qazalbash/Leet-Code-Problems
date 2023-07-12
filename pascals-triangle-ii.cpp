// https://leetcode.com/problems/pascals-triangle-ii

class Solution {
public:
    vector<int> getRow(int rowIndex) {
        size_t row[rowIndex + 1];
        row[0] = 1ul;
        row[rowIndex] = 1ul;

        for(size_t i = 1ul; 2ul * i < rowIndex + 1; ++i) {
            row[i] = row[i-1] * (rowIndex - i + 1) / i;
            row[rowIndex - i] = row[i];
        }
        vector<int> result(row, row + rowIndex + 1);
        return result;
    }
};