// Loop over records in file.

#include <iostream>

#include "dptdb.h"

void loop_forward(dpt::APIFoundSet& foundset)
{
    dpt::APIRecordSetCursor cursor = foundset.OpenCursor();  // Cursor is set on first record.
    if (!cursor.Accessible()) {
        std::cout << "No records for loop_forward\n";
        foundset.CloseCursor(cursor);
        return;
    }
    while (cursor.Accessible()) {
        std::cout << "At record " << cursor.LastAdvancedRecNum() << "\n";
        cursor.Advance();  // Default is 1 meaning each record is visited.
    }
    std::cout << "loop_forward finished\n";
    foundset.CloseCursor(cursor);
}

void loop_backward(dpt::APIFoundSet& foundset)
{
    dpt::APIRecordSetCursor cursor = foundset.OpenCursor();
    cursor.GotoLast();
    if (!cursor.Accessible()) {
        std::cout << "No records for loop_backward\n";
        foundset.CloseCursor(cursor);
        return;
    }
    while (cursor.Accessible()) {
        std::cout << "At record " << cursor.LastAdvancedRecNum() << "\n";
        cursor.Advance(-1);
    }
    std::cout << "loop_backward finished\n";
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
