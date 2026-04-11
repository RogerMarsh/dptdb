// load_records_22.cpp
// Add 65281 records to file by normal update with no field-value pairs added to any records.
// Add one key to invisible field in records 0, 1, 2, and 65280, with value "0".
// The file is created by create_file_75000.

#include <iostream>
#include <string>
#include <sstream>

#include "dptdb.h"

void add_records_no_index(dpt::APIDatabaseFileContext& context)
{
    dpt::APIStoreRecordTemplate record;
    int record_number = context.StoreRecord(record);
    // std::cout << "record " << record_number << " stored" << std::endl;
}

void add_value(dpt::APIDatabaseFileContext& context, const unsigned int recnum, const std::string lookup, const bool report)
{
    dpt::APIFoundSet fs = context.FindRecords(dpt::APIFindSpecification(dpt::FD_SINGLEREC, recnum));
    dpt::APIRecordSetCursor c = fs.OpenCursor();
    while (c.Accessible()) {
        dpt::APIRecord r = c.AccessCurrentRecordForReadWrite();
        r.AddField("Lookup", lookup);
        c.Advance();
    }
    fs.CloseCursor(c);
    context.DestroyRecordSet(fs);
    if (report)
        std::cout << "Lookup field added to record " << recnum << std::endl;
}

int main()
{
    std::cout << "enter load_records_22" << std::endl;

    // Parms argument for Normal mode.  The first two arguments are the default values.
    dpt::APIDatabaseServices dbserv("sysprint.txt", "George", "parms_normal.ini");

    dbserv.Allocate("TSTSMALL", "testsmall.dpt");
    dpt::APIContextSpecification spec = dpt::APIContextSpecification("TSTSMALL");
    dpt::APIDatabaseFileContext context = dbserv.OpenContext(spec);
    // Add 65281 records not indexed.
    for (int i = 0; i < 65281; ++i) {
        add_records_no_index(context);
    };
    // Add Lookup field to records 0, 1, 2, 65280, with "0" as index value.
    add_value(context, 0, "0", true);
    add_value(context, 1, "0", true);
    add_value(context, 2, "0", true);
    add_value(context, 65280, "0", true);
    dbserv.Commit();
    std::cout << "65281 records stored 4 records on one key" << std::endl;
    dbserv.CloseContext(context);
    std::cout << "context closed" << std::endl;
    dbserv.Free("TSTSMALL");
    std::cout << "leave load_records_22" << std::endl;
}
