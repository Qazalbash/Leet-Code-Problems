// https://leetcode.com/problems/excel-sheet-column-title

class Solution {
public:
    string convertToTitle(int columnNumber) {
        --columnNumber;
        string title = "";
        do {
            title = (char)(columnNumber % 26 + 65) + title;
            columnNumber = columnNumber / 26 - 1;
        } while (columnNumber>=0);
        
        return title;
    }
};