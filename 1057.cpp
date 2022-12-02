#include <iostream>
using namespace std;

int main()
{
    int N, num1, num2, round;
    cin >> N >> num1 >> num2; 

    round = 1;
    while (N > 2)
    {
        if ((num2 - num1 == 1 && num2 % 2 == 0) || (num1 - num2 == 1 && num1 % 2 == 0))
            break;
        else
        {
            if (num1 % 2 == 0)
            {
                num1 = num1 / 2;
            }
            else
            {
                num1 = (num1 + 1) / 2;
            }

            if (num2 % 2 == 0)
            {
                num2 = num2 / 2;
            }
            else
            {
                num2 = (num2 + 1) / 2;
            }

            round++;
        }
    }
    cout << round << endl;

    return 0;
}

//
//
//
//
// 1 2 #4라운드
// 1 2 3 4 #3라운드
// 1 2 3 4 5 6 7 8 #2라운드
// (1 2) (3 4) (5 6) (7 8) (9 10) (11 12) (13 14) (15 16) #1라운드