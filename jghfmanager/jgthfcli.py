
import json
import os

import sys

#import jgcmlib as jcm

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))


def main():
  from cminferencer import main as cminferencer_main
  cminferencer_main()
  
if __name__ == "__main__":
  main()