#include <iostream>
#include <vector>
using namespace std;

int N, delNode, parent[50];
vector<vector<int>> tree;
vector<int> result, visited(50, 0);

void maketree(vector<vector<int>> &tree)
{
    for (int i = 0; i < N; i++)
    {
        vector<int> row;
        for (int j = 0; j < N; j++)
        {
            if (parent[j] == i)
                row.push_back(j);
        }
        tree.push_back(row);
    }
}

void findleaf(int start)
{
    visited[start] = 1;
    cout << "현재 노드: " << start << endl;
    if (tree[start].size() == 0)
    {
        result.push_back(start);
    }
    else
    {
        for (int i = 0; i < tree[start].size(); i++)
        {
            if (visited[tree[start][i]] == 0)
                findleaf(tree[start][i]);
        }
    }
}

int main()
{
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        cin >> parent[i];
    }
    cin >> delNode;

    int root;
    for (int i = 0; i < N; i++)
    {
        if (parent[i] == -1)
            root = i;
    }

    if (delNode == root)
        cout << 0;
    else
    {
        parent[delNode] = -99;
        maketree(tree);
        findleaf(root);
        cout << result.size();
    }
}