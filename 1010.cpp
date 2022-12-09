#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int T, N, M, arr[30][30];
vector<int> result;

int build(int n, int k)
{
    if (arr[n][k] > 0)
        return arr[n][k];
    if (n == k)
        return arr[n][k] = 1;
    if (k == 1)
        return arr[n][k] = n;
    return arr[n][k] = build(n - 1, k - 1) + build(n - 1, k);
}

int main()
{
    cin >> T;
    for (int i = 0; i < T; i++)
    {
        cin >> N >> M;
        result.push_back(build(M, N));
    }

    for (int i = 0; i < result.size(); i++)
    {
        cout << result[i] << endl;
    }
}