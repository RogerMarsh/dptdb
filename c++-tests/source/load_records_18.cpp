// Add 65281 records to file by single-step deferred update with one key indexing 2 records segment 0.
// The file is created by create_file_75000.

#include <iostream>
#include <string>

#include "dptdb.h"

void add_records_no_index(dpt::APIDatabaseFileContext& context, const std::string data)
{
    dpt::APIStoreRecordTemplate record;
    record.Append("Data", data);
    int record_number = context.StoreRecord(record);
    // std::cout << "record " << record_number << " stored\n";
}

void add_record(dpt::APIDatabaseFileContext& context, const std::string data, const std::string lookup, const bool report)
{
    dpt::APIStoreRecordTemplate record;
    record.Append("Data", data);
    record.Append("Lookup", lookup);
    int record_number = context.StoreRecord(record);
    if (report)
        std::cout << "record " << record_number << " stored\n";
}

void add_two_records(dpt::APIDatabaseFileContext& context, const std::string lookup)
{
    for (int i = 0; i < 2; ++i) {
        add_record(context, lookup, lookup, false);
    };
}

int main()
{
    std::cout << "enter load_records_18\n";

    // Parms argument for DUSingle mode.  The first two arguments are the default values.
    dpt::APIDatabaseServices dbserv("sysprint.txt", "George", "parms_dusingle.ini");

    dbserv.Allocate("TSTSMALL", "testsmall.dpt");
    dpt::APIContextSpecification spec = dpt::APIContextSpecification("TSTSMALL");
    dpt::APIDatabaseFileContext context = dbserv.OpenContext_DUSingle(spec);
    // Add 2 records.
    for (int i = 0; i < 1; ++i) {
        add_two_records(context, std::to_string(i));
    };
    // Add 65278 records not indexed.
    for (int i = 0; i < 65278; ++i) {
        add_records_no_index(context, std::to_string(i));
    };
    // Add 1 record repeating an index value.
    for (int i = 0; i < 1; ++i) {
        add_record(context, std::to_string(i), std::to_string(i), true);
    };
    std::cout << "65281 records stored 3 records on one key\n";
    dbserv.CloseContext(context);
    std::cout << "context closed\n";
    dbserv.Free("TSTSMALL");
    std::cout << "leave load_records_18\n";
}
