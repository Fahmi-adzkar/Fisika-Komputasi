# module error
"""
err(string)
prints 'string' and terminates program
"""
import sys

def err(string):
    print(string)
    input('Press return to exit')
    sys.exit()
