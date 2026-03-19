// Loop over records in file.
// The file is created by create_fields or create_invisible_fields.
// Best to populate file with create_records.

#include <iostream>

#include "dptdb.h"

void loop_forward(dpt::APIFoundSet& foundset)
{
    std::cout << "enter loop_forward" << std::endl;
    dpt::APIRecordSetCursor cursor = foundset.OpenCursor();  // Cursor is set on first record.
    if (!cursor.Accessible()) {
        std::cout << "No records for loop_forward" << std::endl;
        foundset.CloseCursor(cursor);
        return;
    }
    while (cursor.Accessible()) {
        std::cout << "At record " << cursor.LastAdvancedRecNum() << std::endl;
        cursor.Advance();  // Default is 1 meaning each record is visited.
    }
    std::cout << "leave loop_forward" << std::endl;
    foundset.CloseCursor(cursor);
}

void loop_backward(dpt::APIFoundSet& foundset)
{
    std::cout << "enter loop_backward" << std::endl;
    dpt::APIRecordSetCursor cursor = foundset.OpenCursor();
    cursor.GotoLast();
    std::cout << "Accessible " << cursor.Accessible() << " after GotoLast" << std::endl;
    if (!cursor.Accessible()) {
        std::cout << "No records for loop_backward" << std::endl;
        foundset.CloseCursor(cursor);
        return;
    }
    while (cursor.Accessible()) {
        std::cout << "At record " << cursor.LastAdvancedRecNum() << std::endl;
        cursor.Advance(-1);
        std::cout << "Accessible " << cursor.Accessible() << " after Advance" << std::endl;
    }
    std::cout << "leave loop_backward" << std::endl;
    foundset.CloseCursor(cursor);
}

int main()
{
    dpt::APIDatabaseServices dbserv;
    dbserv.Allocate("TSTFIELD", "testfield.dpt");  // File must already exist.
    dpt::APIContextSpecification spec = dpt::APIContextSpecification("TSTFIELD");
    dpt::APIDatabaseFileContext context = dbserv.OpenContext(spec);
    dpt::APIFoundSet foundset = context.FindRecords();
    loop_forward(foundset);
    loop_backward(foundset);
    context.DestroyRecordSet(foundset);
    dbserv.CloseContext(context);
    dbserv.Free("TSTFIELD");
}
