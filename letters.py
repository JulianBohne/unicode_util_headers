
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

# Just something interesting about identifiew parsing: https://www.unicode.org/reports/tr31/

import re

def extract_property(input_file_path: str, property_name: str, output_property_name: str = None):
    property_pattern = re.compile(f'.*;\s*{property_name}\s*#.*')
    if output_property_name is None:
        output_property_name = property_name
    output_file_name = f'unicode_is_{output_property_name.lower()}.h'
    define_name = f'UNICODE_IS_{output_property_name.upper()}'
    function_name = f'u_is_{output_property_name.lower()}'
    num_codepoints = 0

    with open(input_file_path) as input, open('output/' + output_file_name, 'w') as output:
        output.write(f'\n#ifndef {define_name}\n')
        output.write(f'#define {define_name}\n\n')
        output.write('#include <stdint.h>\n\n')
        output.write(f'bool {function_name}(uint32_t code_point) {{\n')
        output.write('    switch(code_point) {\n')
        for line in input:
            if not property_pattern.match(line):
                continue
            
            splits = line[:14].split('..') # The 14 reaches just before the ; in the file
            for num in range(int(splits[0], 16), int(splits[-1], 16) + 1):
                output.write(f'        case {hex(num)}:\n')
                num_codepoints += 1
        output.write('            return true;\n')
        output.write('        \n')
        output.write('        default:\n')
        output.write('            return false;\n')
        output.write('    }\n')
        output.write('}\n')
        output.write('\n')
        output.write(f'#endif // {define_name}\n')
        print(f'Extracted {num_codepoints} code points with property \'{property_name}\' from \'{input_file_path}\'')

extract_property('data/PropList.txt', 'White_Space', 'whitespace')

extract_property('data/DerivedCoreProperties.txt', 'Alphabetic', 'alpha')
