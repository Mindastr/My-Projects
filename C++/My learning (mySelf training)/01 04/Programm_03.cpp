#include <iostream>
#include <windows.h>

using namespace std;

int main()
{
    // 1. Оголошення константи та масиву (наприклад, на 10 елементів)
    const int n = 10;
    int a[n];

    // 2. Введення послідовності чисел з клавіатури
    cout << "Vvedit " << n << " tsilykh chysel:" << endl;
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }

    // 3. Запам'ятовуємо перше число (це елемент з індексом 0)
    int first = a[0];

    // 4. Пошук найменшого числа (алгоритм з Прикладу 3 твоєї методички)
    int min_val = a[0];
    for (int i = 1; i < n; i++)
    {
        if (a[i] < min_val)
        {
            min_val = a[i];
        }
    }

    // 5. Визначення різниці: найменше - перше
    int riznytsia = min_val - first;

    // 6. Виведення результатів на екран
    cout << "Pershe chyslo = " << first << endl;
    cout << "Naymenshe chyslo = " << min_val << endl;
    cout << "Riznytsia mizh naymenshym i pershym = " << riznytsia << endl;

    system("pause");
    return 0;
}