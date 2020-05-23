#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    x = fct(*args)
    try:
        return x
    except Exceptions as err:
        print("Exception: {}".format(err), file=sys.stderr)
