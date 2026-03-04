#include <iostream>

int main() {

    int age = 0;
    double weight = 0.0;

    std::cout << "Enter your age: ";
    if (!(std::cin >> age)) return 1;

    std::cout << "Enter your weight: ";
    if (!(std::cin >> weight)) return 1;

    std::cout << "Age: " << age << "\tWeight: " << weight << std::endl;

    return 0;
}