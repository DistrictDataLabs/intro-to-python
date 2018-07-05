#!/usr/bin/env python
# clock
# Prints out the time specially formatted
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Sat Mar 08 15:29:47 2014 -0500
# Author:   Sarah Kelley <sarahlkelley@gmail.com.com>
# Edited:   Fri Apr 18 00:57:42 EDT 2014
#
# Copyright (C) 2014 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: clock.py [] benjamin@bengfort.com $

"""
Prints out the time specially formatted
"""

##########################################################################
## Imports
##########################################################################

import sys
from datetime import datetime
from dateutil.tz import tzlocal

##########################################################################
## A Clock Printer Object
##########################################################################

class Clock(object):

    # The "default" formats. Add more formats via subclasses or in the
    # instantation of a Clock object (or just add more here).

    # These formats are more complicated string formatting
    FORMATS = {
        "code":"%a %b %d %H:%M:%S %Y %z",
        "json":"%Y-%m-%dT%H:%M:%S.%fZ",
        "cute":"%b %d, %Y",
    }

    # class method - bound to the class
    # Get the current time
    # tzlocal will get the local timezone
    @classmethod
    def local_now(klass):
        return datetime.now(tzlocal())

    def __init__(self, formats={}):
        self.formats = self.FORMATS.copy()
        self.formats.update(formats)

    # strftime takes a format and returns a string representing the date
    def _local_format(self, fmt):
        return Clock.local_now().strftime(fmt)

    def get_stamp(self, name):
        # strips "-" from beginning and end of string
        # the string is "-code", "-json" or "-cute"
        name  = name.strip("-")

        if name in self.formats:
            return self._local_format(self.formats[name])

        return None

    def print_stamp(self, name):
            stamp = self.get_stamp(name)
            if stamp:
                print(stamp)
            else:
                print("No stamp format for name %s" % name)

##########################################################################
## Main Method, handle inputs to program from command line
##########################################################################

# print __name__ in the python shell to see how this works
if __name__ == "__main__":

    args  = sys.argv[1:]
    clock = Clock()
    for arg in args:
        clock.print_stamp(arg)
