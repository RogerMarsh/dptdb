// Find records in file by FD_POINT$ and FD_NOT_POINT$.

#include <iostream>

#include "dptdb.h"

// APIDatabaseFileContext constructor takes a 'const int&' argument.
void point(dpt::APIDatabaseFileContext& context, const int position)
{
    dpt::APIFindSpecification findspec = dpt::APIFindSpecification(dpt::FD_POINT$, position);
    dpt::APIFoundSet foundset = context.FindRecords(findspec);
    std::cout << foundset.Count() << " records found point for position " << position << "\n";
    context.DestroyRecordSet(foundset);
}

// APIDatabaseFileContext constructor takes a 'const int&' argument.
void not_point(dpt::APIDatabaseFileContext& context, const int position)
{
    dpt::APIFindSpecification findspec = dpt::APIFindSpecification(dpt::FD_NOT_POINT$, position);
    dpt::APIFoundSet foundset = context.FindRecords(findspec);
    std::cout << foundset.Count() << " records found not_point for position " << position << "\n";
    context.DestroyRecordSet(foundset);
}

int main()
{
    dpt::APIDatabaseServices dbserv;
    dbserv.Allocate("TSTFIELD", "testfield.dpt");  // File must already exist.
    dpt::APIContextSpecification spec = dpt::APIContextSpecification("TSTFIELD");
    dpt::APIDatabaseFileContext context = dbserv.OpenContext(spec);
    point(context, 1000000);  // Segment > 0
    not_point(context, 1000000);
    point(context, 10000);  // Segment 0
    not_point(context, 10000);
    point(context, 6);
    not_point(context, 6);
    point(context, 0);
    not_point(context, 0);
    point(context, -2);  // Point$MaskOff method gets 0 as absrec argument, not -2.
    not_point(context, -2);  // Point$MaskOff method gets 0 as absrec argument, not -2.
    point(context, -10000);  // Point$MaskOff method gets 0 as absrec argument, not -10000.
    not_point(context, -10000);  // Point$MaskOff method gets 0 as absrec argument, not -10000.
    point(context, -1000000);  // Point$MaskOff method gets 0 as absrec argument, not -1000000.
    not_point(context, -1000000);  // Point$MaskOff method gets 0 as absrec argument, not -1000000.
    dbserv.CloseContext(context);
    dbserv.Free("TSTFIELD");
}
