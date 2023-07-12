// https://leetcode.com/problems/sort-an-array

class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        mergeSort(nums, 0, nums.size()-1);
        return nums;
    }
private:

    void merge(vector<int>& arr, int p, int q, int r) {
        const int n1 = q - p + 1, n2 = r - q;
        
        int L[n1], M[n2];
        
        for (int i = 0; i < n1; i++)
            L[i] = arr[p + i];
        
        for (int j = 0; j < n2; j++)
            M[j] = arr[q + 1 + j];

        int i = 0, j = 0, k = p;
    
        while (i < n1 && j < n2) arr[k++] = (L[i] <= M[j]) ? L[i++] : M[j++];
        while (i < n1) arr[k++] = L[i++];
        while (j < n2) arr[k++] = M[j++];
    }

    void mergeSort(vector<int>& arr, const int l, const int r) {
        if (l < r) {
            const int m = (r + l) >> 1;
            mergeSort(arr, l, m);
            mergeSort(arr, m + 1, r);
            merge(arr, l, m, r);
        }
    }
    
};