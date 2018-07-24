import sys
import core

__author__ = 'kole'

def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]

    print("WU TANG FINANCIAL")
    print("C.R.E.A.M.\n")
    core.execute_me()

    # Do argument parsing here (eg. with argparse) and anything else
    # you want your project to do.

if __name__ == "__main__":
    main()