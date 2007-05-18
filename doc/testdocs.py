import doctest
import sys

simulator = sys.argv[-1]

exec("from pyNN.%s import *" % simulator)

setup(max_delay=1.0)
#doctest.testfile('lowlevelapi.txt',globs=globals(),optionflags=doctest.IGNORE_EXCEPTION_DETAIL)
doctest.testfile('highlevelapi.txt',globs=globals(),optionflags=doctest.IGNORE_EXCEPTION_DETAIL)

