
#ifndef UNICODE_IS_WHITESPACE
#define UNICODE_IS_WHITESPACE

#include <stdint.h>

bool u_is_whitespace(uint32_t code_point) {
    switch(code_point) {
        case 0x9:
        case 0xa:
        case 0xb:
        case 0xc:
        case 0xd:
        case 0x20:
        case 0x85:
        case 0xa0:
        case 0x1680:
        case 0x2000:
        case 0x2001:
        case 0x2002:
        case 0x2003:
        case 0x2004:
        case 0x2005:
        case 0x2006:
        case 0x2007:
        case 0x2008:
        case 0x2009:
        case 0x200a:
        case 0x2028:
        case 0x2029:
        case 0x202f:
        case 0x205f:
        case 0x3000:
            return true;
        
        default:
            return false;
    }
}
#endif // UNICODE_IS_WHITESPACE
