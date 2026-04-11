// api_sequential_services.cpp
// Allocate and Free two sequential files and explicitly close database services.
// Note the equivalent 'Free's fail in load_records_23.cpp where they are also
// named in the OpenContext_DUMulti(...) call.

#include <iostream>

#include "dptdb.h"

int main()
{
    std::cout << "enter api_sequential_services" << std::endl;
    dpt::APIDatabaseServices api;
    dpt::APISequentialFileServices seq = api.SeqServs();
    std::cout << "allocate sequential files" << std::endl;
    seq.Allocate("TAPEA", "tapea.txt", dpt::FILEDISP_NEW);
    seq.Allocate("TAPEN", "tapen.txt", dpt::FILEDISP_NEW);
    std::cout << "free sequential files" << std::endl;
    seq.Free("TAPEA");
    seq.Free("TAPEN");
    std::cout << "destroy database services" << std::endl;
    api.Destroy();
    std::cout << "leave api_sequential_services" << std::endl;
}
