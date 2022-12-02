#include <iostream>
#include <queue>
#include <vector>
using namespace std;
using pii = pair<int, int>;

int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};
int farm[51][51];
int visited[51][51];
int T, M, N, K, X, Y;
vector<pii> cabbage;
vector<int> v;
vector<int> result;

int bfs(int row, int col)
{
    if (visited[row][col] == 1)
        return -1;
    visited[row][col] = 1;
    int cnt = 1;
    queue<pii> q;
    q.push({row, col});
    while (!q.empty())
    {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        for (int i = 0; i < 4; i++)
        {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (nx < 0 || nx >= M || ny < 0 || ny >= N)
            {
                continue;
            }
            if (visited[nx][ny] == 1 || farm[nx][ny] == 0)
            {
                continue;
            }
            q.push({nx, ny});
            visited[nx][ny] = 1;
            cnt++;
        }
    }

    return cnt;
}

int main()
{
    cin >> T;
    for (int i = 0; i < T; i++)
    {
        v.clear();
        cabbage.clear();

        for (int j = 0; j < 51; j++)
        {
            for (int k = 0; k < 51; k++)
            {
                farm[j][k] = 0;
                visited[j][k] = 0;
            }
        }

        cin >> M >> N >> K;
        for (int j = 0; j < K; j++)
        {
            cin >> X >> Y;
            cabbage.push_back({X, Y});
            farm[X][Y] = 1;
        }
        for (int k = 0; k < cabbage.size(); k++)
        {
            if (bfs(cabbage[k].first, cabbage[k].second) != -1)
                v.push_back(bfs(cabbage[k].first, cabbage[k].second));
        }

        result.push_back(v.size());
    }

    if (result.size() == 0)
        cout << 0;
    else
    {
        for (int i = 0; i < result.size(); i++)
        {
            cout << result[i] << endl;
        }
    }

    return 0;
}