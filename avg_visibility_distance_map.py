#!/usr/bin/env python

import sys
import re

for line in sys.stdin:
  val = line.strip()
  (USAFID,visibility_distance,q) = (val[4:10], val[78:84],val[84:85])  
  if (visibility_distance != "999999" and re.match("[01459]", q)):
       print "%s\t%s" %(USAFID ,visibility_distance)


