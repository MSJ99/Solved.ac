#include <iostream>
#include <cctype>
using namespace std;

int partition(long long N, int &L)
{
    while (L <= 100)
    {
        double sumOfFL = double(N * 2) / L;
        if (sumOfFL - int(sumOfFL) == 0)
        {
            double x = double((sumOfFL) - L + 1) / 2;
            if (x >= 0 && x - int(x) == 0)
            {
                return x;
            }
        }
        L++;
    }
    return -1;
}

void print(int v, int L)
{
    for (int i = 0; i < L; i++)
    {
        cout << v + i << " ";
    }
}

int main()
{
    long long N;
    int L;
    cin >> N >> L;

    if (partition(N,L) != -1)
    {
        print(partition(N, L), L);
    }
    else
    {
        cout << -1;
    }

    return 0;
}