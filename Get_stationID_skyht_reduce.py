#!/usr/bin/env python

import sys

last_group = None
for line in sys.stdin:
  val = line.strip()
  (USAFID,skyht) = val.split("\t")
  print val
   

