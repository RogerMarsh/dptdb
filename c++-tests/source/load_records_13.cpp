// Add 65281 records to 75000 record file by single-step deferred update with each key indexing 6 records.

#include <iostream>
#include <string>

#include "dptdb.h"

void add_record(dpt::APIDatabaseFileContext& context, const std::string data, const std::string lookup)
{
    dpt::APIStoreRecordTemplate record;
    record.Append("Data", data);
    record.Append("Lookup", lookup);
    int record_number = context.StoreRecord(record);
    // std::cout << "record " << record_number << " stored\n";
}

void add_six_records(dpt::APIDatabaseFileContext& context, const std::string lookup)
{
    for (int i = 0; i < 6; ++i) {
        add_record(context, lookup, lookup);
    };
}

int main()
{
    std::cout << "enter load_records_13\n";

    // Parms argument for DUSingle mode.  The first two arguments are the default values.
    dpt::APIDatabaseServices dbserv("sysprint.txt", "George", "parms_dusingle.ini");

    dbserv.Allocate("TSTSMALL", "testsmall.dpt");
    dpt::APIContextSpecification spec = dpt::APIContextSpecification("TSTSMALL");
    dpt::APIDatabaseFileContext context = dbserv.OpenContext_DUSingle(spec);
    // Add 65280 records.
    for (int i = 0; i < 10880; ++i) {
        add_six_records(context, std::to_string(i));
    };
    // Add 1 record repeating an index value.
    for (int i = 0; i < 1; ++i) {
        add_record(context, std::to_string(i), std::to_string(i));
    };
    std::cout << "65281 records stored 6 records per key\n";
    dbserv.CloseContext(context);
    std::cout << "context closed\n";
    dbserv.Free("TSTSMALL");
    std::cout << "leave load_records_13\n";
}
