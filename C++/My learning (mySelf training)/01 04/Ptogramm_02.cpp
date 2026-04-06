#include <iostream>
#include <windows.h>

using namespace std;

int main()
{
    const int n = 5;
    double a[n];

    cout << "Enter 5 real numbers:" << endl;
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }

    double min_val = a[0];
    double max_val = a[0];

    for (int i = 1; i < n; i++)
    {
        if (a[i] < min_val)
        {
            min_val = a[i];
        }

        if (a[i] > max_val)
        {
            max_val = a[i];
        }
    }

    cout << "Min element = " << min_val << endl;
    cout << "Max element = " << max_val << endl;

    system("pause");
    return 0;
}