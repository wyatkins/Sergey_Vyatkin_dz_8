#!/usr/bin/env python3

import re

PARSE_RE = re.compile(
    r"""(?P<addres>^\S+)[\s-]*\[(?P<datatime>.*)\]\s*\"(?P<resp>\w*)\s*(?P<file>[/\w]+)[^\"]+\"\s+(?P<code>\d+)\s+(?P<size>\d+)""")
# r"""(?P<addres>^((\d|[a-fA-F]){0,4}[\.\:]?){4,8})[\s-]*\[(?P<datatime>.*)\]\s*\"(?P<req>\w*)\s*(?P<file>[/\w]+)[^\"]+\"\s+(?P<code>\d+)\s+(?P<size>\d+)""")

with open("./nginx_logs", "r", encoding="utf-8") as file:
    print(*(tuple(x.groupdict().values())
            for line in file for x in PARSE_RE.finditer(line)), sep="\n")