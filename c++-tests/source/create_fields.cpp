// Create a file with two fields, one of them indexed.

#include "dptdb.h"

void create_field(dpt::APIDatabaseFileContext& context, const std::string name, bool index)
{
    dpt::APIFieldAttributes attributes = dpt::APIFieldAttributes(false, false, false, index, false, 50, false, false);
    context.DefineField(name, attributes);
}

int main()
{
    dpt::APIDatabaseServices dbserv;
    dbserv.Allocate("TSTFIELD", "testfield.dpt", dpt::FILEDISP_COND);
    dbserv.Create("TSTFIELD");  // DD name is 8 characters maximum.
    dpt::APIContextSpecification spec = dpt::APIContextSpecification("TSTFIELD");
    dpt::APIDatabaseFileContext context = dbserv.OpenContext(spec);
    context.Initialize(false);  // The default: I think it means existing stuff is wiped out.
    create_field(context, "Data", false);
    create_field(context, "Lookup", true);
    dbserv.CloseContext(context);
    dbserv.Free("TSTFIELD");
}
