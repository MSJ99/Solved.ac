#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int N, M, V;
int v1, v2;
int graph[1001][1001];
int visited[1001];

void dfs(int start)
{
    visited[start] = 1;
    cout << start << " ";
    for (int i = 0; i <= N; i++)
    {
        if (graph[start][i] == 1)
        {
            if (visited[i] == 0)
            {
                dfs(i);
            }
        }
    }
}

void bfs(int start)
{
    queue<int> q;
    q.push(start);
    visited[start] = 1;
    while (!q.empty())
    {
        int current = q.front();
        cout << current << " ";
        q.pop();
        for (int i = 0; i <= N; i++)
        {
            if (graph[current][i] == 1)
            {
                if (visited[i] == 0)
                {
                    q.push(i);
                    visited[i] = 1;
                }
            }
        }
    }
}

int main()
{
    cin >> N >> M >> V;
    for (int i = 0; i <= N; i++)
    {
        for (int j = 0; j <= N; j++)
        {
            graph[i][j] = 0;
        }
    }
    for (int i = 0; i < M; i++)
    {
        cin >> v1 >> v2;
        graph[v1][v2] = 1;
        graph[v2][v1] = 1;
    }

    for (int i = 0; i <= N; i++)
    {
        visited[i] = 0;
    }
    dfs(V);

    cout << endl;

    for (int i = 0; i <= N; i++)
    {
        visited[i] = 0;
    }
    bfs(V);

    return 0;
}