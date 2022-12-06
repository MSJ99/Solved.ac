#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N, vote;
vector<int> candidate;

void steal(vector<int> &candidate, int num)
{
    candidate[0] += 1;
    candidate[num + 1] -= 1;
}

bool isMax(vector<int> candidate)
{
    for (int i = 1; i < candidate.size(); i++)
    {
        if (candidate[0] <= candidate[i])
            return false;
    }
    return true;
}

bool boundary(vector<int> candidate)
{
    for (int i = 0; i < candidate.size(); i++)
    {
        if (*max_element(candidate.begin() + 1, candidate.end()) == 1)
        {
            return false;
        }
    }
    return true;
}

int lobby(vector<int> candidate, int cnt)
{
    while (!isMax(candidate) && boundary(candidate))
    {
        steal(candidate, max_element(candidate.begin() + 1, candidate.end()) - (candidate.begin() + 1));
        cnt++;
    }
    return cnt;
}

int main()
{
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        cin >> vote;
        candidate.push_back(vote);
    }

    cout << lobby(candidate, 0);
}
/*
    [5 7 7] -> [6 6 7] -> [7 6 6]: 2회
    [10 10 10 10] -> [11 9 10 10]: 1회
    [1 1] -> [2 0] X, 득표수는 자연수이므로 불가: 0회
    [5 10 7 3 8] -> [9 7 7 3 7]: 4회
*/