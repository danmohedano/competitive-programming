#include <bits/stdc++.h>

using namespace std;

int sum_first_n(int n){
    // 1 + 2 + ... + n
    return n * (n + 1) / 2; 
}

int sum_first_n_sqr(int n){
    // 1^2 + 2^2 + ... + n^2
    return n * (n + 1) * (2 * n + 1) / 6;
}

int sum_arithmetic(int a, int b, int n){
    // a + ... + b (n numbers)
    return n * (a + b) / 2;
}

int sum_geometric(int a, int b, int k){
    // a + ak + ak^2 + ... + b
    return (b * k - a) / (k - 1);
}

int max_subarray_sum(vector<int> array){
    int best = 0, sum = 0;
    for (auto & el : array){
        sum = max(el, sum + el);
        best = max(best, sum);
    }

    return best;
}