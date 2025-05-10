/*binary_search*/
#include <bits/stdc++.h>
using namespace std;

template <typename T>
int binarySearch(vector<T>& v, T target) {
    auto it = lower_bound(v.begin(), v.end(), target);
    if (it != v.end() && *it == target) {
        return it - v.begin();
    } else {
        return -1;
    }
}