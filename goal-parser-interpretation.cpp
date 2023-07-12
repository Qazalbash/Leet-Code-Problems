// https://leetcode.com/problems/goal-parser-interpretation

class Solution {
public:
    string interpret(string command) {
        string r = "";
        const int n = command.size();
        for (int i = 0; i < n; ++i) {
            if (command[i] == '(') {
                if (command[i + 1] == ')') {
                    r += 'o';
                    ++i;
                } else {
                    r += "al";
                    i += 3;
                }
            } else {
                r += command[i];
            }
        }
        return r;
    }
};