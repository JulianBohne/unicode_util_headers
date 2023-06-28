
# http://www.unicode.org/reports/tr44/#General_Category_Values

# All the property text files:
# https://www.unicode.org/Public/UCD/latest/ucd/

# This one contains the Alphabetic property:
# https://www.unicode.org/Public/UCD/latest/ucd/DerivedCoreProperties.txt
#                              ...
# 0041..005A    ; Alphabetic # L&  [26] LATIN CAPITAL LETTER A..LATIN CAPITAL LETTER Z
# 0061..007A    ; Alphabetic # L&  [26] LATIN SMALL LETTER A..LATIN SMALL LETTER Z
#                              ...

# This one contains the White_Space property:
# https://www.unicode.org/Public/UCD/latest/ucd/PropList.txt
#                              ...
# 0009..000D    ; White_Space # Cc   [5] <control-0009>..<control-000D>
# 0020          ; White_Space # Zs       SPACE
#                              ...


with open('white_space.txt') as alphabetic_file, open('unicode_is_whitespace.h', 'w') as output:
    output.write("\n#ifndef UNICODE_IS_WHITESPACE\n")
    output.write("#define UNICODE_IS_WHITESPACE\n\n")
    output.write("#include <stdint.h>\n\n")
    output.write("bool u_is_whitespace(uint32_t code_point) {\n")
    output.write("    switch(code_point) {\n")
    for line in alphabetic_file:
        splits = line[:14].split("..") # The 14 reaches just before the ; in the file
        for num in range(int(splits[0], 16), int(splits[-1], 16) + 1):
            output.write(f"        case {hex(num)}:\n")
    output.write("            return true;\n")
    output.write("        \n")
    output.write("        default:\n")
    output.write("            return false;\n")
    output.write("    }\n")
    output.write("}\n")
    output.write("#endif // UNICODE_IS_WHITESPACE\n")

with open('alphabetic.txt') as alphabetic_file, open('unicode_is_alphabetic.h', 'w') as output:
    output.write("\n#ifndef UNICODE_IS_ALPHABETIC\n")
    output.write("#define UNICODE_IS_ALPHABETIC\n\n")
    output.write("#include <stdint.h>\n\n")
    output.write("bool u_is_alphabetic(uint32_t code_point) {\n")
    output.write("    switch(code_point) {\n")
    for line in alphabetic_file:
        splits = line[:14].split("..") # The 14 reaches just before the ; in the file
        for num in range(int(splits[0], 16), int(splits[-1], 16) + 1):
            output.write(f"        case {hex(num)}:\n")
    output.write("            return true;\n")
    output.write("        \n")
    output.write("        default:\n")
    output.write("            return false;\n")
    output.write("    }\n")
    output.write("}\n")
    output.write("#endif // UNICODE_IS_ALPHABETIC\n")

