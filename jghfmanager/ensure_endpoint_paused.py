import json
import os

import jgcmlib as jcm

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from jgthfdata import JgHfConfig, JgHfMusicalPieces


def main():
  config_filename="orpheus-config.yml"
  #if not found try read from $HOME
  if not os.path.exists(config_filename):
    config_filename=os.path.join(os.getenv("HOME"),config_filename)
    if not os.path.exists(config_filename):
      print(f"Error: {config_filename} not found")
      exit()


  config=JgHfConfig(config_filename)
  #print(config.huggingface)


  # Step 2: Import necessary modules
  from huggingface_hub import HfApi
  from huggingface_hub import InferenceEndpoint

  # Step 3: Authenticate using your HuggingFace token
  api = HfApi()
  _api_key_name="HUGGINGFACE_API_KEY"

  if 'token_env_var' in config.huggingface:
    _api_key_name=config.huggingface['token_env_var']
  token = os.getenv(_api_key_name)

  # Step 4: Start the specified inference endpoint
  name=config.huggingface['name']
  namespace=config.huggingface['namespace']
  repository=config.huggingface['repository']



  endpoint:InferenceEndpoint=api.get_inference_endpoint(name=name,namespace=namespace,token=token)
  

  print("Endpoint status (before we ensure its off): ",endpoint.status)
  print(endpoint)



  endpoint.pause()
  endpoint:InferenceEndpoint=api.get_inference_endpoint(name=name,namespace=namespace,token=token)
  print("Endpoint status (after we ensure its off): ",endpoint.status)
  print(endpoint)
 
  import time
  start_time = time.time()


  if endpoint.status=='paused':
    print("Endpoint is already paused")
    exit()

  if endpoint.status!='paused':
    while endpoint.status!='paused':
      endpoint:InferenceEndpoint=api.get_inference_endpoint(name=name,namespace=namespace,token=token)
      #print(endpoint)
      #print three dots without enters
      print(".", end="")
      #wait 3 seconds
      time.sleep(1)
      print(".", end="")
      time.sleep(1)
      print(".", end="")
      time.sleep(1)
      print("Waiting for endpoint to pause")
  end_time = time.time()
  print(f"Pause time: {end_time-start_time} seconds")
  time.sleep(1)


if __name__ == "__main__":
  main()

