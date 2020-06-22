#!/usr/bin/env python3

# based on http://www.firestik.com/Tech_Docs/SWRLOSS.htm

import sys

if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + " SWR")
    sys.exit(1)

swr = float(sys.argv[1])
loss = (swr-1)*(swr-1)/((swr+1)*(swr+1))
print("Power loss: {:.2f}%".format(100*loss))
