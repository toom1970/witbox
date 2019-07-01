import os
import re
from optparse import OptionParser

if os.getuid() != 0:
    print("must run as super user!")
    exit()


def usage():
    print("usage:  --isopath/-p <iso path> --volume/-m <mount point>")


parser = OptionParser()
parser.add_option(
    "--volume",
    "-m",
    action="store",
    dest="root",
    default=False,
    help="usage:  --isopath/-p <iso path> --volume/-m <mount point>")
parser.add_option(
    "--isopath",
    "-p",
    action="store",
    dest="repo",
    default=False,
    help="usage:  --isopath/-p <iso path> --volume/-m <mount point>")

(options, args) = parser.parse_args()

if options.root:
    root = options.root
    print(root)
if options.repo:
    repo = options.repo
    print(repo)
root = re.sub("/+$", "", root)
part = ""





