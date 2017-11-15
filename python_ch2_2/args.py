# command line의 arguments 처리
# -f hello.py
import sys
print(sys.argv)

args = sys.argv[1:]
print(args)