
import json
import os
import sys
import argparse

#import jgcmlib as jcm

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))


def main():
  parser = argparse.ArgumentParser(description='OHFI - Orpheus HuggingFace Inference tool')
  
  args, unknown = parser.parse_known_args()
  
  if '--help' in sys.argv or '-h' in sys.argv:
    parser.print_help()
    return
  
  from cminferencer import main as cminferencer_main
  cminferencer_main()
  
if __name__ == "__main__":
  main()