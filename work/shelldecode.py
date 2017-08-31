#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import sys 

def main():

    for line in sys.stdin:
        sys.stdout.write(re.sub(r'\\u\w{4}',
            lambda e: unichr(int(e.group(0)[2:], 16)).encode('utf-8'), 
            line))

if __name__ == '__main__':
    main()
