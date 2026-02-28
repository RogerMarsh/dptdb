// Unsigned short comparison for equality with zero.

#include <iostream>

// Simple version of FindNextRelRec method with the comparison.
class Segment {
public:
    bool compare_with_zero(unsigned short& number) const;
};

bool Segment::compare_with_zero(unsigned short& number) const
{
    if (number == 0) {
	std::cout << number << " compares equal to 0\n";
	return false;
	}
    std::cout << number << " compares not equal to 0\n";
    return true;
}

// Real code has methods in other classes which calculate and return an unsigned short.
unsigned short one() {return 1;};
unsigned short zero() {return 0;};
unsigned short minus_one() {return -1;};

void compare(unsigned short number) {
    Segment segment;
    bool answer;
    answer = segment.compare_with_zero(number);
}

int main()
{
    compare(one());
    compare(zero());
    compare(minus_one());
}
