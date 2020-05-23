#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        x = fct(*args)
        return x
    except Exceptions as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return None
