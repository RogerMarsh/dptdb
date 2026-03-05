// Add 65280 records to file by single-step deferred update with each key indexing 7 records.
// The file is created by create_file_75000.

#include <iostream>
#include <string>

#include "dptdb.h"

void add_record_no_index(dpt::APIDatabaseFileContext& context, const std::string data)
{
    dpt::APIStoreRecordTemplate record;
    record.Append("Data", data);
    int record_number = context.StoreRecord(record);
    // std::cout << "record " << record_number << " stored\n";
}

void add_record(dpt::APIDatabaseFileContext& context, const std::string data, const std::string lookup)
{
    dpt::APIStoreRecordTemplate record;
    record.Append("Data", data);
    record.Append("Lookup", lookup);
    int record_number = context.StoreRecord(record);
    // std::cout << "record " << record_number << " stored\n";
}

void add_seven_records(dpt::APIDatabaseFileContext& context, const std::string lookup)
{
    for (int i = 0; i < 7; ++i) {
        add_record(context, lookup, lookup);
    };
}

int main()
{
    std::cout << "enter load_records_10\n";

    // Parms argument for DUSingle mode.  The first two arguments are the default values.
    dpt::APIDatabaseServices dbserv("sysprint.txt", "George", "parms_dusingle.ini");

    dbserv.Allocate("TSTSMALL", "testsmall.dpt");
    dpt::APIContextSpecification spec = dpt::APIContextSpecification("TSTSMALL");
    dpt::APIDatabaseFileContext context = dbserv.OpenContext_DUSingle(spec);
    // Add 65275 records.
    for (int i = 0; i < 9325; ++i) {
        add_seven_records(context, std::to_string(i));
    };
    // Add 5 records.
    for (int i = 0; i < 5; ++i) {
        add_record_no_index(context, std::to_string(i));
    };
    std::cout << "65280 records stored 7 records per key\n";
    dbserv.CloseContext(context);
    std::cout << "context closed\n";
    dbserv.Free("TSTSMALL");
    std::cout << "leave load_records_10\n";
}
