#include <iostream>

using namespace std;

class line
{
public:
    void print();
    void solve();
    int N;
    int order[10];
    int result[10];
};

void line::print()
{
    for (int i = 0; i < N; i++) {
        cout << result[i] << " ";
    }
}

void line::solve()
{
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        order[i] = 11;
        result[i] = 11;
    }
    for (int i = 0; i < N; i++)
    {
        cin >> order[i];
    }

    for (int i = 0; i < N; i++)
    {
        int cnt = 0;
        for (int j = 0; j < N; j++)
        {
            if (i+1 < result[j])
            {
                if (cnt == order[i])
                {
                    if (result[j] == 11)
                    {
                        result[j] = i + 1;
                    }
                }
                cnt++;
            }
        }
    }
}

int main() 
{
    line a;
    a.solve();
    a.print();

    return 0;
}

// 6  1  1  1  2  0  0
// 11 2  3  4  11 1  11