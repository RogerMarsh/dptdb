// Create a file for 75000 records with two fields, one of them indexed and invisible.

// This file will accept one batch of 65280 records with a few thousand to spare.
// Each segment of a file holds 65280 record slots.

#include "dptdb.h"

void create_field(dpt::APIDatabaseFileContext& context, const std::string name, bool index, bool invisible)
{
    dpt::APIFieldAttributes attributes = dpt::APIFieldAttributes(false, invisible, false, index, false, 50, false, false);
    context.DefineField(name, attributes);
}

int main()
{
    dpt::APIDatabaseServices dbserv;
    dbserv.Allocate("TSTSMALL", "testsmall.dpt", dpt::FILEDISP_COND);
    dbserv.Create("TSTSMALL",  // DD name is 8 characters maximum.
        375,      // bsize (pages)
        200,      // brecppg (so file can hold 150000 records maximum without being extended)
        -1,       // breserve (-1 means take default as argument)
        -1,       // breuse
        400,      // dsize
        -1,       // dreserve
        -1,       // dpgsres
        dpt::FILEORG_UNORD_RRN);  // fileorg
    dpt::APIContextSpecification spec = dpt::APIContextSpecification("TSTSMALL");
    dpt::APIDatabaseFileContext context = dbserv.OpenContext(spec);
    context.Initialize(false);  // The default: existing stuff is wiped out.
    create_field(context, "Data", false, false);
    create_field(context, "Lookup", true, true);
    dbserv.CloseContext(context);
    dbserv.Free("TSTSMALL");
}
