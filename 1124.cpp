#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int factorize(int n)
{
    int cnt = 0;
    int factor = 2;
    while (n != 1)
    {
        if (n % factor == 0)
        {
            n = n / factor;
            cnt++;
        }
        else
        {
            factor++;
        }
    }
    return cnt;
}

int main()
{
    int A, B;
    vector<int> v;
    vector<int> result;
    v.clear();
    result.clear();
    for (int i = A; i <= B; i++)
    {
        v.push_back(i);
    }

    for (int i = 0; i < v.size(); i++)
    {
        result[i] = factorize(v[i]);
    }

    int factor = 2;
    int mul = 0;

    while (factor != *max_element(result.begin(), result.end()))
    {
        if (result[mul] % factor == 0)
        {
            result[mul] = 0;
            mul++;
        }
        factor++;
    }

    int cnt = 0;
    for (int i = 0; i < result.size(); i++)
    {
        if (result[i] != 0)
        {
            cnt++;
        }
    }

    cout << cnt;

    return 0;
}