// Loop over index entries for field in file.

#include <iostream>
#include <string>

#include "dptdb.h"

void loop_forward(dpt::APIDatabaseFileContext& context)
{
    // Cursor is set on first index value.  Default direction is dpt::CURSOR_ASCENDING.
    dpt::APIDirectValueCursor cursor = context.OpenDirectValueCursor("Lookup");  // Lookup created in create_fields.
    if (!cursor.Accessible()) {
        std::cout << "No values for loop_forward\n";
        context.CloseDirectValueCursor(cursor);
        return;
    }
    while (cursor.Accessible()) {
        dpt::APIFieldValue value = cursor.GetCurrentValue();
        std::string string_value = value.ExtractString();  // Field may be ORD NUM or ORD CHAR.
        std::cout << "At value " << string_value << "\n";
        cursor.Advance();  // Default is 1 meaning each value is visited in direction order.
    }
    std::cout << "loop_forward finished\n";
    context.CloseDirectValueCursor(cursor);
}

void loop_backward(dpt::APIDatabaseFileContext& context)
{
    // Cursor is set on last index value.
    dpt::APIDirectValueCursor cursor = context.OpenDirectValueCursor("Lookup", dpt::CURSOR_DESCENDING);
    if (!cursor.Accessible()) {
        std::cout << "No values for loop_backward\n";
        context.CloseDirectValueCursor(cursor);
        return;
    }
    while (cursor.Accessible()) {
        dpt::APIFieldValue value = cursor.GetCurrentValue();
        std::string string_value = value.ExtractString();  // Field may be ORD NUM or ORD CHAR.
        std::cout << "At value " << string_value << "\n";
        cursor.Advance();  // Default is 1 meaning each value is visited in direction order.
    }
    std::cout << "loop_backward finished\n";
    context.CloseDirectValueCursor(cursor);
}

int main()
{
    dpt::APIDatabaseServices dbserv;
    dbserv.Allocate("TSTFIELD", "testfield.dpt");  // File must already exist.
    dpt::APIContextSpecification spec = dpt::APIContextSpecification("TSTFIELD");
    dpt::APIDatabaseFileContext context = dbserv.OpenContext(spec);
    loop_forward(context);
    loop_backward(context);
    dbserv.CloseContext(context);
    dbserv.Free("TSTFIELD");
}
