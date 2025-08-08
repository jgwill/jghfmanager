
import json
import os
import sys
import argparse

#import jgcmlib as jcm

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))


def main():
  parser = argparse.ArgumentParser(description='OHFI - Orpheus HuggingFace Inference tool')
  parser.add_argument('--help', action='store_true', help='Show this help message and exit')
  
  args, unknown = parser.parse_known_args()
  
  if args.help or '--help' in sys.argv:
    parser.print_help()
    return
  
  from cminferencer import main as cminferencer_main
  cminferencer_main()
  
if __name__ == "__main__":
  main()