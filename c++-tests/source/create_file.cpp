// Create a file.

#include "dptdb.h"

int main()
{
    dpt::APIDatabaseServices dbserv;
    dbserv.Allocate("TESTFILE", "testfile.dpt", dpt::FILEDISP_COND);
    dbserv.Create("TESTFILE");
    dpt::APIContextSpecification spec = dpt::APIContextSpecification("TESTFILE");
    dpt::APIDatabaseFileContext context = dbserv.OpenContext(spec);
    context.Initialize(true);  // Not compatible with multiple B or D extents.  See dbctxt.cpp (~1080).
    dbserv.CloseContext(context);
    dbserv.Free("TESTFILE");
}
