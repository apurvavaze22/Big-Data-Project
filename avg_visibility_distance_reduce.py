#!/usr/bin/env python

import sys
(last_key, count, sum) = (None, 0, 0)
for line in sys.stdin:
  (key, val) = line.strip().split("\t")
  if last_key and last_key != key:
    print("%s\t%s" % (last_key, sum / count))
    (last_key, count, sum) = (key, 1, int(val))
  else:
    (last_key, count, sum) = (key, count + 1, sum + int(val))

if last_key:
  print("%s\t%s" %(last_key, sum / count))










