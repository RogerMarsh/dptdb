// Add 10 records to file by single-step deferred update indexed by same key.

#include <iostream>

#include "dptdb.h"

void add_record(dpt::APIDatabaseFileContext& context, const std::string data, const std::string lookup)
{
    dpt::APIStoreRecordTemplate record;
    record.Append("Data", data);
    record.Append("Lookup", lookup);
    int record_number = context.StoreRecord(record);
    std::cout << "record " << record_number << " stored\n";
}

int main()
{
    std::cout << "enter load_records_02\n";

    // Parms argument for DUSingle mode.  The first two arguments are the default values.
    dpt::APIDatabaseServices dbserv("sysprint.txt", "George", "parms_dusingle.ini");

    dbserv.Allocate("TSTFIELD", "testfield.dpt");
    dpt::APIContextSpecification spec = dpt::APIContextSpecification("TSTFIELD");
    dpt::APIDatabaseFileContext context = dbserv.OpenContext_DUSingle(spec);
    add_record(context, "100", "e");
    add_record(context, "200", "e");
    add_record(context, "300", "e");
    add_record(context, "400", "e");
    add_record(context, "500", "e");
    add_record(context, "600", "e");
    add_record(context, "700", "e");
    add_record(context, "800", "e");
    add_record(context, "900", "e");
    add_record(context, "000", "e");
    dbserv.CloseContext(context);
    dbserv.Free("TSTFIELD");
    std::cout << "leave load_records_02\n";
}
