#!/usr/bin/env python

import re
import sys

for line in sys.stdin:
  val = line.strip()
  (USAFID,skyht,q) = (val[4:10], val[70:75],val[75:76])  
  if (skyht != "99999" and re.match("[01459]", q)):
    print "%s\t%s" % (USAFID, skyht)



