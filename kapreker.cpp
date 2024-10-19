#include <iostream>
#include <cmath>
#include <vector>
#include <string>

bool isKaprekar(int number, int base) {
    // Calculate the square of the number
    long long squared = static_cast<long long>(number) * number;

    // Convert the squared number to the specified base and store it as a string
    std::string squaredStr;
    while (squared > 0) {
        squaredStr.insert(squaredStr.begin(), '0' + (squared % base));
        squared /= base;
    }

    // Check different splits of the squared number
    int length = squaredStr.length();
    for (int i = 1; i < length; ++i) {
        // Split the string into two parts
        std::string leftStr = squaredStr.substr(0, i);
        std::string rightStr = squaredStr.substr(i);

        // Convert the two parts back to the specified base
        int left = leftStr.empty() ? 0 : std::stoi(leftStr, nullptr, base);
        int right = rightStr.empty() ? 0 : std::stoi(rightStr, nullptr, base);

        // Check if the sum of the two parts equals the original number
        if (left + right == number) {
            return true;
        }
    }

    return false;
}

int main() {
    int number, base;

    std::cout << "Enter the number to check: ";
    std::cin >> number;
    std::cout << "Enter the base (2 or greater): ";
    std::cin >> base;

    if (base < 2) {
        std::cerr << "Base must be 2 or greater!" << std::endl;
        return 1;
    }

    if (isKaprekar(number, base)) {
        std::cout << number << " is a Kaprekar number in base " << base << "." << std::endl;
    } else {
        std::cout << number << " is not a Kaprekar number in base " << base << "." << std::endl;
    }

    return 0;
}
