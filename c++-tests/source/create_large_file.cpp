// Create a large file with two fields, one of them indexed and invisible.

#include "dptdb.h"

void create_field(dpt::APIDatabaseFileContext& context, const std::string name, bool index, bool invisible)
{
    dpt::APIFieldAttributes attributes = dpt::APIFieldAttributes(false, invisible, false, index, false, 50, false, false);
    context.DefineField(name, attributes);
}

int main()
{
    dpt::APIDatabaseServices dbserv;
    dbserv.Allocate("TSTLARGE", "testlarge.dpt", dpt::FILEDISP_COND);
    dbserv.Create("TSTLARGE",  // DD name is 8 characters maximum.
        750,      // bsize (pages)
        200,      // brecppg (so file can hold 150000 records maximum without being extended)
        -1,       // breserve (-1 means take default as argument)
        -1,       // breuse
        400,      // dsize
        -1,       // dreserve
        -1,       // dpgsres
        dpt::FILEORG_UNORD_RRN);  // fileorg
    dpt::APIContextSpecification spec = dpt::APIContextSpecification("TSTLARGE");
    dpt::APIDatabaseFileContext context = dbserv.OpenContext(spec);
    context.Initialize(false);  // The default: existing stuff is wiped out.
    create_field(context, "Data", false, false);
    create_field(context, "Lookup", true, true);
    dbserv.CloseContext(context);
    dbserv.Free("TSTLARGE");
}
