// load_records_24.cpp
// Add 65281 records to file by normal update with no field-value pairs added to any records.
// Place records 0, 1, 2, and 65280, on a list and file records under 'Lookup == "0"'.
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

void add_record_to_list(dpt::APIDatabaseFileContext& context, dpt::APIRecordList& list, const unsigned int recnum)
{
    dpt::APIFoundSet fs = context.FindRecords(dpt::APIFindSpecification(dpt::FD_SINGLEREC, recnum));
    list.Place(fs);
    context.DestroyRecordSet(fs);
    std::cout << "Record " << recnum << " added to list" << std::endl;
}

int main()
{
    std::cout << "enter load_records_24" << std::endl;

    // Parms argument for Normal mode.  The first two arguments are the default values.
    dpt::APIDatabaseServices dbserv("sysprint.txt", "George", "parms_normal.ini");

    dbserv.Allocate("TSTSMALL", "testsmall.dpt");
    dpt::APIContextSpecification spec = dpt::APIContextSpecification("TSTSMALL");
    dpt::APIDatabaseFileContext context = dbserv.OpenContext(spec);
    // Add 65281 records not indexed.
    for (int i = 0; i < 65281; ++i) {
        add_records_no_index(context);
    };
    // Add records 0, 1, 2, 65280, to list and file under 'Lookup == "0"'.
    dpt::APIRecordList lookup = context.CreateRecordList();
    add_record_to_list(context, lookup, 0);
    add_record_to_list(context, lookup, 1);
    add_record_to_list(context, lookup, 2);
    add_record_to_list(context, lookup, 65280);
    context.FileRecordsUnder(lookup, "Lookup", "0");
    dbserv.Commit();
    std::cout << "65281 records stored 4 records on one key" << std::endl;
    context.DestroyRecordSet(lookup);
    dbserv.CloseContext(context);
    std::cout << "context closed" << std::endl;
    dbserv.Free("TSTSMALL");
    std::cout << "leave load_records_24" << std::endl;
}
