#ifndef Q658_H
#define Q658_H

#include <vector>
#include <iostream>
using namespace std;

class Q658
{
public:
    Q658();

    /**Faster than 15.91%
     * @brief findClosestElements
     * @param arr
     * @param k
     * @param x
     * @return
     */
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        vector<int> buf;
        int l = arr.size();

        if (l == 0) return buf;
        else if (x <= arr[0]) {
            arr.resize(k);
            return arr;
        }
        else if (x >= arr[l-1]) {
            vector<int> sub(arr.end() - k, arr.end());
            return sub;
        }
        else {
            int lo = 0, hi = l, mid = l / 2;
            while (lo < mid && mid < hi) {
                if (arr[mid] > x) hi = mid;
                else if (arr[mid] < x) lo = mid;
                else break;

                mid = (lo + hi) / 2;
            }

            // x != arr[mid]
            if (x != arr[mid] && x - arr[mid] > arr[hi] - x)
                mid = hi;
            else if (x != arr[mid])
                mid = lo;
            buf.insert(buf.end(), arr[mid]);

            // cout << buf[0] << lo << mid << hi << endl;
            lo = mid, hi = mid;
            while (buf.size() < k) {
                if (0 < lo && hi+1 < l && x - arr[lo - 1] <= arr[hi+1] - x) {
                    buf.insert(buf.begin(), arr[lo - 1]);
                    lo--;
                }
                else if (hi+1 < l) {
                    buf.insert(buf.end(), arr[hi+1]);
                    hi++;
                }
                else if (0 < lo) {
                    buf.insert(buf.begin(), arr[lo - 1]);
                    lo--;
                }
                else
                    break;

            }
        }
        return buf;
    }
};

#endif // Q658_H
