// basic_sizes.cpp
// Show size of types: short, int, long, long long.
// DPT assumes thes are 2, 4, 4, and 8, respectively.

#include <iostream>

int main()
{
    std::cout << "short: " << sizeof(short);
    std::cout << "   int: " << sizeof(int);
    std::cout << "   long: " << sizeof(long);
    std::cout << "   long long: " << sizeof(long long);
    std::cout << std::endl;
}
