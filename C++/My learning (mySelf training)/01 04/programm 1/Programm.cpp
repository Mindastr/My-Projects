#include <iostream>
#include <windows.h> 

using namespace std;

int main() {
    const int n = 10;
    int numbers[n];

    cout << "Enter " << n << " elements:" << endl;
    for (int i = 0; i < n; i++) {
        cin >> numbers[i];
    }

    int count = 0;
    int sum = 0;

    for (int i = 0; i < n; i++) {
        if (numbers[i] % 5 == 0) {
            count++;
            sum = sum + numbers[i];
        }
    }

    if (count == 0) {
        cout << "Елементів кратних 5 в масиві немає" << endl;
    } else {
        cout << "Count = " << count << endl;
        cout << "Sum = " << sum << endl;
    }

    system("pause");
    return 0;
}