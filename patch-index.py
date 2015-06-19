from __future__ import absolute_import, division, print_function

import codecs
import os.path as path
import re

SEARCH_INDEX_PATH = path.join('target', 'doc', 'search-index.js')
DEPS = [
    'stats', 'tabwriter', 'cbor', 'quickcheck', 'regex', 'byteorder',
    'suffix', 'csv', 'docopt',
    'regex_syntax', 'memchr', 'aho-corasick',
]

sidx = list(map(unicode.strip,
                codecs.open(SEARCH_INDEX_PATH, encoding='utf-8')))
new_idx = codecs.open(SEARCH_INDEX_PATH, 'w+', encoding='utf-8')
for line in sidx:
    m = re.search(r"^searchIndex\['(\w+)'\]", line)
    if not m or m.group(1) in DEPS:
        print(line, file=new_idx)
