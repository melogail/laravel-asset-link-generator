#! python3

import re, functions as fn
from os import path

## This program is for changing <img> tags path and <script> tags
## to asset() function with path within.

## Open and read targeted file
file = fn.check_sys_arg(index=1, error_message="Error...You forget to add file path!",
                        input_message="Please specify file path")
start_pattern = fn.check_sys_arg(index=2, error_message="Error...You forget to specify start pattern!",
                                 input_message="Please add start pattern")

# try to read file lines
lines = None

try:
    with open(file, 'rt') as fp:
        lines = fp.read().splitlines()
except:
    fn.check_sys_arg(index=1, error_message="Error...File doesn't exist!",
                     input_message="Please specify file path")

## Open and write to targeted file
with open(file, 'wt') as fp:
    for line in lines:
        ## Get the path from the pattern
        if re.search(r'"' + start_pattern + '(.*?)"', line):
            path = re.search(r'"' + start_pattern + '(.*?)"', line).group(1)

            change = re.sub(r'"' + start_pattern + '(.*?)"', line, '{{asset("' + path + '")}}')
            ## Rewrite the whole file again
            fp.write(line.replace(start_pattern + path, change))

        else:
            fp.write(line)
