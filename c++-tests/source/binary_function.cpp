// Copy-typed from 
// learn.microsoft.com/en-us/cpp/standard-library/binary-function-struct?view=msvc-170
// using hints from
// stackoverflow.com/questions/57236763/how-to-change-binary-function-to-c17-code
// to not depend on std::binary_function.
// Hints:
// Replace inheritance from std::binary_function with the typedef's for
// first_argument_type, second_argument_type, and return_type to keep
// the code working pre-c++17.
// At c++17 and later the code will likely work with just the inheritance
// removed: no extra typedefs, so in this example first_argument_type,
// second_argument_type, and result_type, in the definition of operator
// are replaced by double.

#include <vector>
#include <functional>
#include <algorithm>
#include <iostream>

template <class Type> class average
{
    typedef double first_argument_type;
    typedef double second_argument_type;
    typedef double result_type;
public:
    result_type operator() (first_argument_type a, second_argument_type b)
    {
        return (result_type) ((a+b)/2);
    }
};

int main()
{
    std::vector <double> v1, v2, v3 (6);
    std::vector <double>::iterator Iter1, Iter2, Iter3;

    for (int i=1; i<=6; i++)
        v1.push_back(11.0/i);

    for (int j=0; j<=5; j++)
        v2.push_back(-2.0*j);

    std::cout << "The vector v1 = ( ";
    for (Iter1=v1.begin(); Iter1 != v1.end(); Iter1++)
        std::cout << *Iter1 << " ";
    std::cout << ")" << std::endl;

    std::cout << "The vector v2 = ( ";
    for (Iter2=v2.begin(); Iter2 != v2.end(); Iter2++)
        std::cout << *Iter2 << " ";
    std::cout << ")" << std::endl;

    // Finding the element-wise averages of the elements of v1 and v2.
    std::transform(v1.begin(), v1.end(), v2.begin(), v3.begin(), average<double>());

    std::cout << "The element-wise averages are: ( ";
    for (Iter3=v3.begin(); Iter3 != v3.end(); Iter3++)
        std::cout << *Iter3 << " ";
    std::cout << ")" << std::endl;
}
