# Step 1: Install the huggingface_hub library
# Run this command in your terminal
# pip install huggingface_hub

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
  #print(endpoint)


  musical_pieces_filename="musical.yml"
  musical_pieces=JgHfMusicalPieces(musical_pieces_filename)
  print(musical_pieces)

  cname=musical_pieces.musical['name']

  sname=musical_pieces.musical['sname']

  prompts=musical_pieces.musical['prompts']

  #exit()
  print(endpoint)
  endpoint.resume()
  endpoint:InferenceEndpoint=api.get_inference_endpoint(name=name,namespace=namespace,token=token)
  print(endpoint)
  #InferenceEndpoint(name='chatmusician-jgwill', namespace='jgwill', repository='m-a-p/ChatMusician', status='running', url='https://tb3fo9kbyxinth5a.us-east-1.aws.endpoints.huggingface.cloud')
  #count boot time
  import time
  start_time = time.time()


  if endpoint.status!='running':
    while endpoint.status!='running':
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
      print("Waiting for endpoint to start")
  end_time = time.time()
  print(f"Boot time: {end_time-start_time} seconds")
  time.sleep(1)

  headers = {
    "Accept" : "application/json",
    "Content-Type": "application/json" 
  }





  try:
    output_json_of_choosen_pieces = f"{cname}_musical_{sname}.json"
    jcm.save_as_json_to_filename(prompts,output_json_of_choosen_pieces)
    for k,v in prompts.items():
      print("-------------------------------------------")
      print(k,v)
      pass
      payload={
        "inputs": v,
        "parameters": {}
          }
      try:
        response = endpoint.client.post(json=payload)
        print(response)

        #Grab the generated text
        response = json.loads(response)[0]
        try:
          output_filename = f"{cname}_{sname}_{k}.json"
          jcm.save_as_json_to_filename(response,output_filename)
          time.sleep(1)
        except:
          print("k:",k,", v:",v, " Error: Could not save response as json")
          pass
      except:
        print("Error in inferences...")
        pass

  except Exception as e:
    print("Error in inferences...")
    print(e)
    print("Suspending the endpoint")      
    endpoint.pause()

    endpoint:InferenceEndpoint=api.get_inference_endpoint(name=name,namespace=namespace,token=token)
    print(endpoint)


  #@STCIssue IN CASE
  endpoint.pause()


  endpoint:InferenceEndpoint=api.get_inference_endpoint(name=name,namespace=namespace,token=token)
  print(endpoint)


if __name__ == "__main__":
  main()