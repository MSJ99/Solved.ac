#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;

bool isException(double x1, double y1, double x2, double y2, double x3, double y3)
{
    if ((x1 == x2) && (y1 == y2))
        return true;
    else if ((x1 == x3) && (y1 == y3))
        return true;
    else if ((x2 == x3) && (y2 == y3))
        return true;
    else
    {
        if (abs(y2 - y1) / abs(x2 - x1) == abs(y3 - y1) / abs(x3 - x1))
            return true;
    }
    return false;
}

int main()
{
    double x1, y1, x2, y2, x3, y3;
    cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3;

    if (isException(x1, y1, x2, y2, x3, y3))
        cout << -1;
    else
    {
        double d1, d2, d3;
        d1 = sqrt((x3 - x2) * (x3 - x2) + (y3 - y2) * (y3 - y2));
        d2 = sqrt((x3 - x1) * (x3 - x1) + (y3 - y1) * (y3 - y1));
        d3 = sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1));

        double sq1, sq2, sq3;
        sq1 = 2 * (d2 + d3);
        sq2 = 2 * (d1 + d3);
        sq3 = 2 * (d1 + d2);

        printf("%.16f", max({sq1, sq2, sq3}) - min({sq1, sq2, sq3}));
    }
}