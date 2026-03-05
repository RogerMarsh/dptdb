// Add 900 records to file by single-step deferred update indexed by same key.
// The file is created by create_file_150000.

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
    std::cout << "enter load_records_03\n";

    // Parms argument for DUSingle mode.  The first two arguments are the default values.
    dpt::APIDatabaseServices dbserv("sysprint.txt", "George", "parms_dusingle.ini");

    dbserv.Allocate("TSTLARGE", "testlarge.dpt");
    dpt::APIContextSpecification spec = dpt::APIContextSpecification("TSTLARGE");
    dpt::APIDatabaseFileContext context = dbserv.OpenContext_DUSingle(spec);
    for (int i = 0; i < 900; ++i) {
        add_record(context, std::to_string(i), "e");
    };
    std::cout << "900 records stored\n";
    dbserv.CloseContext(context);
    std::cout << "context closed\n";
    dbserv.Free("TSTLARGE");
    std::cout << "leave load_records_03\n";
}
