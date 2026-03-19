// Add 65281 records to file by single-step deferred update with one key indexing 3 records in segment 0.
// The file is created by create_file_75000.

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
    record.Append("Data", data);
    int record_number = context.StoreRecord(record);
    // std::cout << "record " << record_number << " stored" << std::endl;
}

void add_record(dpt::APIDatabaseFileContext& context, const std::string data, const std::string lookup, const bool report)
{
    dpt::APIStoreRecordTemplate record;
    record.Append("Data", data);
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
    std::cout << "enter load_records_19" << std::endl;

    // Parms argument for DUSingle mode.  The first two arguments are the default values.
    dpt::APIDatabaseServices dbserv("sysprint.txt", "George", "parms_dusingle.ini");

    dbserv.Allocate("TSTSMALL", "testsmall.dpt");
    dpt::APIContextSpecification spec = dpt::APIContextSpecification("TSTSMALL");
    dpt::APIDatabaseFileContext context = dbserv.OpenContext_DUSingle(spec);
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
    std::cout << "context closed" << std::endl;
    dbserv.Free("TSTSMALL");
    std::cout << "leave load_records_19" << std::endl;
}
