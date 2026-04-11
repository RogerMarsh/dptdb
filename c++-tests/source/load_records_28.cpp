// load_records_28.cpp
// Add  multi-step deferred update with one key indexing 3 records in segment 0.
// This is run after load_records_27.cpp.

#include <iostream>
//#include <string>
//#include <sstream>

#include "dptdb.h"

int main()
{
    std::cout << "enter load_records_28" << std::endl;

    // Parms argument for DUMulti mode.  The first two arguments are the default values.
    dpt::APIDatabaseServices dbserv("sysprint.txt", "George", "parms_dumulti.ini");

    // Allocate the two work files.
    dpt::APISequentialFileServices seq = dbserv.SeqServs();
    seq.Allocate("TAPEA", "tapea.txt");
    seq.Allocate("TAPEN", "tapen.txt");

    dbserv.Allocate("TSTSMALL", "testsmall.dpt");
    dpt::APIContextSpecification spec = dpt::APIContextSpecification("TSTSMALL");
    dpt::APIDatabaseFileContext reopen = dbserv.OpenContext(spec);
    reopen.ApplyDeferredUpdates();
    dbserv.CloseContext(reopen);
    std::cout << "context closed (third step)" << std::endl;

    seq.Free("TAPEA");
    seq.Free("TAPEN");

    dbserv.Free("TSTSMALL");
    std::cout << "leave load_records_28" << std::endl;
}
