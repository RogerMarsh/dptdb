// Unsigned short comparison for equality with zero.
// Verify operation of this comparison which fails in soome cases in record_loop.

#include <iostream>
#include <sstream>

// So this can run at c++98 and c++03 standards too.
std::string int_to_string(const int number)
{
    std::stringstream ss;
    ss << number;
    std::string str = ss.str();
    return str;
}

// Simple version of FindNextRelRec method with the comparison.
class Segment {
public:
    bool compare_with_zero(unsigned short& number) const;
};

bool Segment::compare_with_zero(unsigned short& number) const
{
    if (number == 0) {
	std::cout << int_to_string(number) << " compares equal to 0" << std::endl;
	return false;
	}
    std::cout << int_to_string(number) << " compares not equal to 0" << std::endl;
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
