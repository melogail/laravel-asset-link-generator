#! python3

import re, sys

## This program is for changing <img> tags path and <script> tags
## to asset() function with path within.

## Open and read targeted file
file = sys.argv[1]
start_pattern = sys.argv[2]
with open(file, 'rt') as fp:
    lines = fp.read().splitlines()

## Open and write to targeted file
with open(file, 'wt') as fp:
    for line in lines:
        ## Get the path from the pattern
        if re.search(r'"' + start_pattern + '(.*?)"', line):
            path = re.search(r'"' + start_pattern + '(.*?)"', line).group(1)
            ## Change the path to the desired pattern
            change = re.sub(r'"' + start_pattern + '(.*?)"', line, '{{asset("' + path + '")}}')
            ## Rewrite the whole file again
            fp.write(line.replace(start_pattern + path, change))
        else:
            fp.write(line)

