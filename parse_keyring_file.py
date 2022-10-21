#!/usr/bin/python3
import os
import sys
import optparse

"""grit unittests presubmit script.

See http://dev.chromium.org/developers/how-tos/depottools/presubmit-scripts for
details on the presubmit API built into gcl.
"""

# 检查python版本
if sys.version_info < (3, 0):
  sys.exit("GRIT requires Python 3.0 or later.")

EOF_TAG_SIZE = 3


def ParseFile(file_path):
  # r+b mode is open the binary file in read or write mode.
  file = open(file_path, 'rb')
  fsize = os.path.getsize(file.name)
  print("文件总字节数：{}".format(fsize))


def main(argv):
  parser = optparse.OptionParser()
  parser.add_option("-v", "--verbose", dest="verbose")
  # parse cmdline arguments to an object
  # then pass to main
  (options, args) = parser.parse_args()
  if len(args) != 1:
    parser.error("keyring file argument is missing.")
  keyring_file = os.path.realpath(args[0])
  ParseFile(keyring_file)


# Omitted when being used as module
if __name__ == '__main__':
  sys.exit(main(sys.argv[1:]))
