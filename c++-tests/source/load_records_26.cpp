// load_records_26.cpp
// Intended for run after running one of load_records_18 (19, 20, 21, 22, 23, 24, 25).
// Print record count for file and record numders of records indexed by 'Lookup == 0'.
// The file is created by create_file_75000.

#include <iostream>
#include <string>
#include <sstream>

#include "dptdb.h"

void count_records_on_file(dpt::APIDatabaseFileContext& context)
{
    dpt::APIFindSpecification allrecs;
    dpt::APIFoundSet fs = context.FindRecords(allrecs);
    std::cout << fs.Count() << " records on file" << std::endl;
    context.DestroyRecordSet(fs);
}

void count_records_for_value(dpt::APIDatabaseFileContext& context, const std::string lookup)
{
    dpt::APIFindSpecification spec("Lookup", dpt::FD_EQ, lookup);
    dpt::APIFoundSet fs = context.FindRecords(spec);
    dpt::APIRecordSetCursor c = fs.OpenCursor();
    while (c.Accessible()) {
        std::cout << "Record " << c.LastAdvancedRecNum() << " has Lookup == '0'" << std::endl;
        c.Advance();
    }
    fs.CloseCursor(c);
    context.DestroyRecordSet(fs);
}

int main()
{
    std::cout << "enter load_records_26" << std::endl;

    // Parms argument for Normal mode.  The first two arguments are the default values.
    dpt::APIDatabaseServices dbserv("sysprint.txt", "George", "parms_normal.ini");

    dbserv.Allocate("TSTSMALL", "testsmall.dpt");
    dpt::APIContextSpecification spec = dpt::APIContextSpecification("TSTSMALL");
    dpt::APIDatabaseFileContext context = dbserv.OpenContext(spec);
    count_records_on_file(context);
    count_records_for_value(context, "0");
    dbserv.CloseContext(context);
    std::cout << "context closed" << std::endl;
    dbserv.Free("TSTSMALL");
    std::cout << "leave load_records_26" << std::endl;
}
