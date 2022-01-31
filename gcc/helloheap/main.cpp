#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

long long heapify(long long N, vector<long long> & vec)
{
    make_heap(vec.begin(), vec.end());
    return vec.front();
}

int main()
{
    ifstream cin;
    cin.open("s2.in");

    long long N;
    cin >> N;
    vector<long long> hi;
    for (long long n = 0; n < N; n++)
    {
        long long h;
        cin >> h;
        hi.push_back(h);
    }

    cout << hi.size() << endl;
    long long frisbee = heapify(N, hi);

    for (long long i : hi)
        cout << i << " ";
    cout << endl;

    hi.push_back(13);
    push_heap(hi.begin(), hi.end());

    hi.push_back(15);
    push_heap(hi.begin(), hi.end());

    for (long long i : hi)
        cout << i << " ";
    cout << endl;

    cout << frisbee << endl;
    for (int i = 0; i < N; i++)
    {
        pop_heap(hi.begin(), hi.end());
        hi.pop_back();
        cout << hi.front() << endl;

        for (long long i : hi)
            cout << i << " ";
        cout << endl;
    }
    cout << endl << hi.size() << endl;

    for (long long i : hi)
        cout << i << " ";
    return 0;
}
