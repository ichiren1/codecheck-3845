#!/usr/bin/env python3
def main(argv):
  for v in argv:
    try:
      num = int(v)
      if num%3 == 0 and v.find("3") >= 0:
        print("dump")
      elif num%3 == 0:
        print("idiot")
      elif v.find("3") >= 0:
        print("stupid")
      else:
        print("smart")
    except ValueError:
      print("invalid")
