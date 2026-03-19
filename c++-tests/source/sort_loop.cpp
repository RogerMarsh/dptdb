// Loop over sorted records in file.
// The file is created by create_fields or create_invisible_fields.
// Best to populate file with create_records.

#include <iostream>

#include "dptdb.h"

dpt::APISortRecordSet sort_ascending(dpt::APIFoundSet& foundset)
{
    dpt::APISortRecordsSpecification specification;
    specification.AddKeyField("Data", dpt::SORT_ASCENDING);  // The default sort order.
    specification.AddDataField("Lookup");
    return foundset.Sort(specification);
}

dpt::APISortRecordSet sort_descending(dpt::APIFoundSet& foundset)
{
    dpt::APISortRecordsSpecification specification;
    specification.AddKeyField("Data", dpt::SORT_DESCENDING);
    specification.AddDataField("Lookup");
    return foundset.Sort(specification);
}

void sort_ascending_loop_forward(dpt::APIFoundSet& foundset)
{
    dpt::APISortRecordSet sortedset = sort_ascending(foundset);
    dpt::APIRecordSetCursor cursor = sortedset.OpenCursor();  // Cursor is set on first record.
    if (!cursor.Accessible()) {
        std::cout << "No records for sort_ascending_loop_forward" << std::endl;
        sortedset.CloseCursor(cursor);
        return;
    }
    while (cursor.Accessible()) {
        std::cout << "At record " << cursor.LastAdvancedRecNum() << std::endl;
        cursor.Advance();  // Default is 1 meaning each record is visited.
    }
    std::cout << "sort_ascending_loop_forward finished" << std::endl;
    sortedset.CloseCursor(cursor);
}

void sort_descending_loop_forward(dpt::APIFoundSet& foundset)
{
    dpt::APISortRecordSet sortedset = sort_descending(foundset);
    dpt::APIRecordSetCursor cursor = sortedset.OpenCursor();  // Cursor is set on first record.
    if (!cursor.Accessible()) {
        std::cout << "No records for sort_descending_loop_forward" << std::endl;
        sortedset.CloseCursor(cursor);
        return;
    }
    while (cursor.Accessible()) {
        std::cout << "At record " << cursor.LastAdvancedRecNum() << std::endl;
        cursor.Advance();  // Default is 1 meaning each record is visited.
    }
    std::cout << "sort_descending_loop_forward finished" << std::endl;
    sortedset.CloseCursor(cursor);
}

void sort_ascending_loop_backward(dpt::APIFoundSet& foundset)
{
    dpt::APISortRecordSet sortedset = sort_ascending(foundset);
    dpt::APIRecordSetCursor cursor = sortedset.OpenCursor();  // Cursor is set on first record.
    cursor.GotoLast();
    if (!cursor.Accessible()) {
        std::cout << "No records for sort_ascending_loop_backward" << std::endl;
        sortedset.CloseCursor(cursor);
        return;
    }
    while (cursor.Accessible()) {
        std::cout << "At record " << cursor.LastAdvancedRecNum() << std::endl;
        cursor.Advance(-1);
    }
    std::cout << "sort_ascending_loop_backward finished" << std::endl;
    sortedset.CloseCursor(cursor);
}

void sort_descending_loop_backward(dpt::APIFoundSet& foundset)
{
    dpt::APISortRecordSet sortedset = sort_descending(foundset);
    dpt::APIRecordSetCursor cursor = sortedset.OpenCursor();  // Cursor is set on first record.
    cursor.GotoLast();
    if (!cursor.Accessible()) {
        std::cout << "No records for sort_descending_loop_backward" << std::endl;
        sortedset.CloseCursor(cursor);
        return;
    }
    while (cursor.Accessible()) {
        std::cout << "At record " << cursor.LastAdvancedRecNum() << std::endl;
        cursor.Advance(-1);
    }
    std::cout << "sort_descending_loop_backward finished" << std::endl;
    sortedset.CloseCursor(cursor);
}

int main()
{
    dpt::APIDatabaseServices dbserv;
    dbserv.Allocate("TSTFIELD", "testfield.dpt");  // File must already exist.
    dpt::APIContextSpecification spec = dpt::APIContextSpecification("TSTFIELD");
    dpt::APIDatabaseFileContext context = dbserv.OpenContext(spec);
    dpt::APIFoundSet foundset = context.FindRecords();
    sort_ascending_loop_forward(foundset);
    sort_descending_loop_forward(foundset);
    sort_ascending_loop_backward(foundset);
    sort_descending_loop_backward(foundset);
    context.DestroyAllRecordSets();  // So explicit destruction of APISortRecordSet instances is avoided.
    dbserv.CloseContext(context);
    dbserv.Free("TSTFIELD");
}
