// Add 1 record to large file by single-step deferred update indexed by same key.

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

int main()
{
    std::cout << "enter load_records_06\n";

    // Parms argument for DUSingle mode.  The first two arguments are the default values.
    dpt::APIDatabaseServices dbserv("sysprint.txt", "George", "parms_dusingle.ini");

    dbserv.Allocate("TSTLARGE", "testlarge.dpt");
    dpt::APIContextSpecification spec = dpt::APIContextSpecification("TSTLARGE");
    dpt::APIDatabaseFileContext context = dbserv.OpenContext_DUSingle(spec);
    for (int i = 0; i < 1; ++i) {
        add_record(context, std::to_string(i), "e");
    };
    std::cout << "1 record stored\n";
    dbserv.CloseContext(context);
    std::cout << "context closed\n";
    dbserv.Free("TSTLARGE");
    std::cout << "leave load_records_06\n";
}
