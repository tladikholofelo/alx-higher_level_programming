#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        return fct(*args)
    except Exception as i:
        print("Exception: {}".format(i), file=sys.stderr)
        return None
