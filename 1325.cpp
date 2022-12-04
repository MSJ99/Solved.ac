#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N, M, trust, trusted, cnt, visited[10001];
vector<int> v, result;
vector<vector<int>> graph;

void dfs(int start)
{
    visited[start] = 1;
    if (graph[start].size() != 0)
    {
        for (int i = 0; i < graph[start].size(); i++)
        {
            if (visited[graph[start][i]] == 0)
            {
                cnt++;
                dfs(graph[start][i]);
            }
        }
    }
}

int main()
{
    cin >> N >> M;
    for (int i = 0; i <= N; i++)
    {
        graph.push_back(v);
    }
    for (int i = 0; i < M; i++)
    {
        cin >> trust >> trusted;
        graph[trusted].push_back(trust);
    }

    for (int i = 0; i <= N; i++)
    {
        for (int j = 0; j <= N; j++)
        {
            visited[j] = 0;
        }
        cnt = 1;
        dfs(i);
        result.push_back(cnt);
    }

    for (int i = 1; i <= N; i++)
    {
        if (result[i] == *max_element(result.begin(), result.end()))
            cout << i << " ";
    }

    return 0;
}