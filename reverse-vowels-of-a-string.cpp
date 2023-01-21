// https://leetcode.com/problems/reverse-vowels-of-a-string

class Solution {
public:
    string reverseVowels(string s) {
        string vov="";
        uint32_t index = 0;
        uint32_t vovs = 0;
        while(s[index] != '\0'){
            if (s[index] == 'a' ||
                s[index] == 'e' ||
                s[index] == 'i' ||
                s[index] == 'o' ||
                s[index] == 'u' ||
                s[index] == 'A' ||
                s[index] == 'E' ||
                s[index] == 'I' ||
                s[index] == 'O' ||
                s[index] == 'U') {
                    vov += s[index];
                    s[index] = '*';
                    vovs++;
                }
            index++;
        }
        index = 0;
        vovs--;
        while(s[index] != '\0') {
            if (s[index] == '*') s[index] = vov[vovs--];
            index++;
        }
        return s;
    }
};