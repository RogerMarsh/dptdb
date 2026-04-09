// bitmap3-init.cpp
// Test bitmap3 constructors in 32-bit and 64-bit builds.

#include <iostream>
#include <cstring>

// These definitions from include/bbglobalsdec.h are needed for
// Msys2 g++ and clang++ builds.
#ifdef __GNUC__
#define _int64 long long
#define _int32 long
#define _int16 short
#define _int8 char
#endif

#include "bitmap3.h"
#include "pagebase.h"

dpt::util::BitMap bitmap_empty()
{
    return dpt::util::BitMap();
}

dpt::util::BitMap bitmap_database_page()
{
    return dpt::util::BitMap(dpt::DBPAGE_BITMAP_SIZE);
}

void bitmap_report(std::string name, dpt::util::BitMap& bm)
{
    std::cout << name << std::endl;
    std::cout << "numbits " << bm.NumBits() << " wholewords " << bm.NumWholeWords() << std::endl;
    std::string bms = bm.ToString();
    std::cout << "bitstring:  length " << bms.length() << " size " << bms.size() << std::endl;
}

void bitmap_bits_set_report_long(std::string name, dpt::util::BitMap& bm)
{
    std::cout << name << std::endl;
    std::cout << "set all bits" << std::endl;
    bm.SetAll(true);
    unsigned long* dvs = reinterpret_cast<unsigned long*>(bm.Data());
    std::cout << dvs << " " << dvs[0] << " .. " << dvs[1019] << " " << dvs[1020] << " .. " << dvs[2039] << " " << dvs[2040] << std::endl;
    std::cout << "unset all bits" << std::endl;
    bm.SetAll(false);
    unsigned long* dvus = reinterpret_cast<unsigned long*>(bm.Data());
    std::cout << dvus << " " << dvus[0] << " .. " << dvus[1019] << " " << dvus[1020] << " .. " << dvus[2039] << " " << dvus[2040] << std::endl;
}

void bitmap_bits_set_report_long_long(std::string name, dpt::util::BitMap& bm)
{
    std::cout << name << std::endl;
    std::cout << "set all bits" << std::endl;
    bm.SetAll(true);
    unsigned long long* dvs = reinterpret_cast<unsigned long long*>(bm.Data());
    std::cout << dvs << " " << dvs[0] << " .. " << dvs[1019] << " " << dvs[1020] << " .. " << dvs[2039] << " " << dvs[2040] << std::endl;
    std::cout << "unset all bits" << std::endl;
    bm.SetAll(false);
    unsigned long long* dvus = reinterpret_cast<unsigned long long*>(bm.Data());
    std::cout << dvus << " " << dvus[0] << " .. " << dvus[1019] << " " << dvus[1020] << " .. " << dvus[2039] << " " << dvus[2040] << std::endl;
}

void bitmap_bits_set_report_size_t(std::string name, dpt::util::BitMap& bm)
{
    std::cout << name << std::endl;
    std::cout << "set all bits" << std::endl;
    bm.SetAll(true);
    size_t* dvs = reinterpret_cast<size_t*>(bm.Data());
    std::cout << dvs << " " << dvs[0] << " .. " << dvs[1019] << " " << dvs[1020] << " .. " << dvs[2039] << " " << dvs[2040] << std::endl;
    std::cout << "unset all bits" << std::endl;
    bm.SetAll(false);
    size_t* dvus = reinterpret_cast<size_t*>(bm.Data());
    std::cout << dvus << " " << dvus[0] << " .. " << dvus[1019] << " " << dvus[1020] << " .. " << dvus[2039] << " " << dvus[2040] << std::endl;
}

int main()
{
    std::cout << "Sizes:  size_t " << sizeof(size_t) << "  long " << sizeof(long) << "  long long " << sizeof(long long)  << std::endl;
    std::cout << "Database Page BitMap size (bits) " << dpt::DBPAGE_BITMAP_SIZE  << std::endl;
    dpt::util::BitMap bm = bitmap_empty();
    bitmap_report("Emtpy bitmap", bm);
    dpt::util::BitMap bmdbp = bitmap_database_page();
    bitmap_report("Database Page bitmap", bmdbp);
    bitmap_bits_set_report_long("Bits set long", bmdbp);
    bitmap_bits_set_report_size_t("Bits set size_t", bmdbp);
    bitmap_bits_set_report_long_long("Bits set long long", bmdbp);
}
