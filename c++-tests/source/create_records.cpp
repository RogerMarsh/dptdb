// Add records to file.

#include "dptdb.h"

void add_record(dpt::APIDatabaseFileContext& context, const std::string data, const std::string lookup)
{
    dpt::APIStoreRecordTemplate record;
    record.Append("Data", data);
    record.Append("Lookup", lookup);
    int record_number = context.StoreRecord(record);
}

int main()
{
    dpt::APIDatabaseServices dbserv;
    dbserv.Allocate("TSTFIELD", "testfield.dpt", dpt::FILEDISP_OLD);  // The default: file must already exist.
    dpt::APIContextSpecification spec = dpt::APIContextSpecification("TSTFIELD");
    dpt::APIDatabaseFileContext context = dbserv.OpenContext(spec);
    add_record(context, "100", "e");
    add_record(context, "200", "f");
    add_record(context, "300", "g");
    add_record(context, "400", "h");
    add_record(context, "500", "i");
    add_record(context, "600", "j");
    add_record(context, "700", "a");
    add_record(context, "800", "b");
    add_record(context, "900", "c");
    add_record(context, "000", "d");
    dbserv.Commit();  // The default.
    dbserv.CloseContext(context);
    dbserv.Free("TSTFIELD");
}
