// load_records_23.cpp
// Add 65281 records to file by multi-step deferred update with one key indexing 3 records in segment 0.
// The file is created by create_file_75000.
// A job like this which includes a sort cannot be done because the 'Free's after step 1 fail.
// load_records_27.cpp and load_records_28.cpp split the task so the sort can be done in between if wanted. 

#include <iostream>
#include <string>
#include <sstream>

#include "dptdb.h"

// So this can run at c++98 and c++03 standards too.
std::string int_to_string(const int number)
{
    std::stringstream ss;
    ss << number;
    std::string str = ss.str();
    return str;
}

void add_records_no_index(dpt::APIDatabaseFileContext& context, const std::string data)
{
    dpt::APIStoreRecordTemplate record;
    int record_number = context.StoreRecord(record);
    // std::cout << "record " << record_number << " stored" << std::endl;
}

void add_record(dpt::APIDatabaseFileContext& context, const std::string data, const std::string lookup, const bool report)
{
    dpt::APIStoreRecordTemplate record;
    record.Append("Lookup", lookup);
    int record_number = context.StoreRecord(record);
    if (report)
        std::cout << "record " << record_number << " stored" << std::endl;
}

void add_three_records(dpt::APIDatabaseFileContext& context, const std::string lookup)
{
    for (int i = 0; i < 3; ++i) {
        add_record(context, lookup, lookup, false);
    };
}

int main()
{
    std::cout << "enter load_records_23" << std::endl;

    // Parms argument for DUMulti mode.  The first two arguments are the default values.
    dpt::APIDatabaseServices dbserv("sysprint.txt", "George", "parms_dumulti.ini");

    // Allocate the two work files.
    dpt::APISequentialFileServices seq = dbserv.SeqServs();
    seq.Allocate("TAPEA", "tapea.txt", dpt::FILEDISP_NEW);
    seq.Allocate("TAPEN", "tapen.txt", dpt::FILEDISP_NEW);

    dbserv.Allocate("TSTSMALL", "testsmall.dpt");
    dpt::APIContextSpecification spec = dpt::APIContextSpecification("TSTSMALL");
    dpt::APIDatabaseFileContext context = dbserv.OpenContext_DUMulti(spec, "TAPEN", "TAPEA");
    // Add 3 records.
    for (int i = 0; i < 1; ++i) {
        add_three_records(context, int_to_string(i));
    };
    // Add 65277 records not indexed.
    for (int i = 0; i < 65277; ++i) {
        add_records_no_index(context, int_to_string(i));
    };
    // Add 1 record repeating an index value.
    for (int i = 0; i < 1; ++i) {
        add_record(context, int_to_string(i), int_to_string(i), true);
    };
    std::cout << "65281 records stored 4 records on one key" << std::endl;
    dbserv.CloseContext(context);
    std::cout << "context closed (first step)" << std::endl;

    // Need not do this because no sort is being done.
    // Also these caused first run to crash.
    // Usually the job would end here and the next two stages would be done in two
    // jobs: Free probably would not be called anyway.
    //seq.Free("TAPEA");
    //seq.Free("TAPEN");

    // The sort (second step) would go here, assuming it is possible to arrange
    // running a sort program or calling a function from a suitable library.
    std::cout << "sort (second step) not used" << std::endl;

    // The load (third step) will work without a sort, but normally not doing the sort
    // would imply the job might as well be done in normal mode.

    // Need not do this because no sort is being done.
    //seq.Allocate("TAPEA", "tapea.txt");
    //seq.Allocate("TAPEN", "tapen.txt");

    dpt::APIDatabaseFileContext reopen = dbserv.OpenContext(spec);
    reopen.ApplyDeferredUpdates();
    dbserv.CloseContext(reopen);
    std::cout << "context closed (third step)" << std::endl;

    dbserv.Free("TSTSMALL");
    std::cout << "leave load_records_23" << std::endl;
}
