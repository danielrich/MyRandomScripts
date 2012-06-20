#!/usr/bin/python

import sys
f = open('/var/log/sudoers', 'w')
if (len(sys.argv) > 1):
   f.write (repr([( argum) for argum in sys.argv]))


f.write("Now to stdin\n")
[f.write(line) for line in sys.stdin.readlines()]
f.close()


