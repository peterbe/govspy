#!/usr/bin/env python
import os

def run():
    indexed = [
        x.strip()
        for x in open('snippets/index.txt').read().splitlines()
        if not x.strip().startswith('#')
    ]
    for d in os.listdir('snippets'):
        fd = os.path.join('snippets', d)
        if os.path.isdir(fd):
            if d not in indexed:
                print d

if __name__ == '__main__':
    run()
