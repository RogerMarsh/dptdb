// Add 65280 records to file by single-step deferred update with each key indexing 1000 records.
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

void add_record_no_index(dpt::APIDatabaseFileContext& context, const std::string data)
{
    dpt::APIStoreRecordTemplate record;
    record.Append("Data", data);
    int record_number = context.StoreRecord(record);
    // std::cout << "record " << record_number << " stored" << std::endl;
}

void add_record(dpt::APIDatabaseFileContext& context, const std::string data, const std::string lookup)
{
    dpt::APIStoreRecordTemplate record;
    record.Append("Data", data);
    record.Append("Lookup", lookup);
    int record_number = context.StoreRecord(record);
    // std::cout << "record " << record_number << " stored" << std::endl;
}

void add_1000_records(dpt::APIDatabaseFileContext& context, const std::string lookup)
{
    for (int i = 0; i < 1000; ++i) {
        add_record(context, lookup, lookup);
    };
}

int main()
{
    std::cout << "enter load_records_14" << std::endl;

    // Parms argument for DUSingle mode.  The first two arguments are the default values.
    dpt::APIDatabaseServices dbserv("sysprint.txt", "George", "parms_dusingle.ini");

    dbserv.Allocate("TSTSMALL", "testsmall.dpt");
    dpt::APIContextSpecification spec = dpt::APIContextSpecification("TSTSMALL");
    dpt::APIDatabaseFileContext context = dbserv.OpenContext_DUSingle(spec);
    // Add 65000 records.
    for (int i = 0; i < 65; ++i) {
        add_1000_records(context, int_to_string(i));
    };
    // Add 280 records not indexed.
    for (int i = 0; i < 280; ++i) {
        add_record_no_index(context, int_to_string(i));
    };
    std::cout << "65280 records stored 1000 records per key" << std::endl;
    dbserv.CloseContext(context);
    std::cout << "context closed" << std::endl;
    dbserv.Free("TSTSMALL");
    std::cout << "leave load_records_14" << std::endl;
}
