#include <iostream>
#include <cmath>
using namespace std;

int main(void)
{
   int t;
   cin >> t;
   int *arr = new int[t];

   int x1, y1, x2, y2;
   int n;

   int ax, ay, ar;
   int length, result;
   for (int i = 0; i < t; i++)
   {
      result = 0;
      cin >> x1 >> y1 >> x2 >> y2;
      length = sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2));

      cin >> n;
      for (int j = 0; j < n; j++)
      {
         cin >> ax >> ay >> ar;
         if (sqrt(pow((x1 - ax), 2) + pow((y1 - ay), 2)) < ar)
         {
            if (sqrt(pow((x2 - ax), 2) + pow((y2 - ay), 2)) > ar)
            {
               result++;
            }
         }
         else if (sqrt(pow((x2 - ax), 2) + pow((y2 - ay), 2)) < ar)
         {
            if (sqrt(pow((x1 - ax), 2) + pow((y1 - ay), 2)) > ar)
            {
               result++;
            }
         }
      }
      arr[i] = result;
   }
   for (int i = 0; i < t; i++)
   {
      cout << arr[i] << endl;
   }

   return 0;
}