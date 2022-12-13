#include <iostream>
#include <queue>
using namespace std;
using pii = pair<int, int>;

int N, lnum, lstart, lend;
priority_queue<pii, vector<pii>, greater<pii>> lec;
priority_queue<int, vector<int>, greater<int>> room;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        cin >> lnum >> lstart >> lend;
        lec.push({lstart, lend});
    }
    room.push(lec.top().second);
    lec.pop();

    while (lec.size() != 0)
    {
        if (room.top() <= lec.top().first)
        {
            room.push(lec.top().second);
            room.pop();
        }
        else
        {
            room.push(lec.top().second);
        }
        lec.pop();
    }

    cout << room.size();
}