// bitmap3-uint32_t-shift.cpp
// Test the bitmap3 shift methods in 32-bit and 64-bit builds.

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

dpt::util::BitMap bitmap_bitsize(uint32_t number_of_bits)
{
    return dpt::util::BitMap(number_of_bits);
}

dpt::util::BitMap bitmap_database_page()
{
    return bitmap_bitsize(dpt::DBPAGE_BITMAP_SIZE);
}

void bitmap_report(std::string name, dpt::util::BitMap& bm)
{
    std::cout << name << std::endl;
    std::cout << "numbits " << bm.NumBits() << " wholewords " << bm.NumWholeWords() << std::endl;
    std::string bms = bm.ToString();
    std::cout << "bitstring:  length " << bms.length() << " size " << bms.size() << std::endl;
}

void set_bit_10_then_shift_left_20_and_right_6(std::string name, dpt::util::BitMap& bm)
{
    std::cout << name << std::endl;
    std::string bms = bm.ToString();
    std::cout << "bitstring:  bits " << bms << "  length " << bms.length() << std::endl;
    bm.Set(10);
    bms = bm.ToString();
    std::cout << "set bit 10  bits " << bms << std::endl;
    bm <<= 20;
    bms = bm.ToString();
    std::cout << "left 20     bits " << bms << std::endl;
    bm >>= 6;
    bms = bm.ToString();
    std::cout << "right 6     bits " << bms << std::endl;
}

void set_top_31_bits_except_top_then_shift_right_64(std::string name, dpt::util::BitMap& bm)
{
    std::cout << name << std::endl;
    std::string bms = bm.ToString();
    std::cout << "bitstring:  bits " << bms << "  length " << bms.length() << std::endl;
    bm.SetRange(65, 94);
    bms = bm.ToString();
    std::cout << "set 30 bits bits " << bms << std::endl;
    bm >>= 64;
    bms = bm.ToString();
    std::cout << "right 64    bits " << bms << std::endl;
}

void set_bottom_31_bits_except_bottom_then_shift_left_64(std::string name, dpt::util::BitMap& bm)
{
    std::cout << name << std::endl;
    std::string bms = bm.ToString();
    std::cout << "bitstring:  bits " << bms << "  length " << bms.length() << std::endl;
    bm.SetRange(1, 30);
    bms = bm.ToString();
    std::cout << "set 30 bits bits " << bms << std::endl;
    bm <<= 64;
    bms = bm.ToString();
    std::cout << "left 64     bits " << bms << std::endl;
}

int main()
{
    std::cout << "Sizes:  uint32_t " << sizeof(uint32_t) << std::endl;
    std::cout << "Database Page BitMap size (bits) " << dpt::DBPAGE_BITMAP_SIZE  << std::endl;
    dpt::util::BitMap bm = bitmap_empty();
    bitmap_report("Emtpy bitmap", bm);
    dpt::util::BitMap bmdbp = bitmap_database_page();
    bitmap_report("Database Page bitmap", bmdbp);
    dpt::util::BitMap bmbb = bitmap_bitsize(32);
    bitmap_report("BitMap of 32 bits", bmbb);
    set_bit_10_then_shift_left_20_and_right_6("Set 1 bit then shift left and right", bmbb);
    dpt::util::BitMap bmbb96a = bitmap_bitsize(96);
    set_top_31_bits_except_top_then_shift_right_64("Set 30 bits then shift right", bmbb96a);
    dpt::util::BitMap bmbb96b = bitmap_bitsize(96);
    set_bottom_31_bits_except_bottom_then_shift_left_64("Set 30 bits then shift left", bmbb96b);
}
