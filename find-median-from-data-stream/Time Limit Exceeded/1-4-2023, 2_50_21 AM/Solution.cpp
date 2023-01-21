// https://leetcode.com/problems/find-median-from-data-stream

class MedianFinder {
public:
    vector<int> v;

    MedianFinder() {}
    
    void addNum(int num) {
        v.push_back(num);
    }
    
    double findMedian() {
        int n = v.size();
        if(n==0) return NULL;
        sort(v.begin(), v.end()); 
        if(n%2) return (double)v[((n+1)>>1)-1];
        n = n >> 1;
        return ((double)(v[n-1]+v[n])/2.0);
    }
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */