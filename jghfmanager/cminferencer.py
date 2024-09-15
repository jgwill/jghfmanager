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

config_filename="orpheus-config.yaml"


config=JgHfConfig(config_filename)
print(config.huggingface)


# Step 2: Import necessary modules
from huggingface_hub import HfApi
from huggingface_hub import InferenceEndpoint

# Step 3: Authenticate using your HuggingFace token
api = HfApi()
_api_key_name="HUGGINGFACE_API_KEY"
token = os.getenv(_api_key_name)

# Step 4: Start the specified inference endpoint
name=config.huggingface['name']
namespace=config.huggingface['namespace']
repository=config.huggingface['repository']



endpoint:InferenceEndpoint=api.get_inference_endpoint(name=name,namespace=namespace,token=token)
print(endpoint)


musical_pieces_filename="musical.yaml"
musical_pieces=JgHfMusicalPieces(musical_pieces_filename)
print(musical_pieces)
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


"""
# Musical Alternations

Am, Bm, Em, Bm, C, D, G

Am, F#, Bm, Em, Am, F#, D, G


# Extracted Musical Progressions:

Am, Bm, Em, Bm, C, D, G

Am, F#, Bm, Em, Am, F#, D, G
"""



cname='Viva'

"""
#@STCGoal INSERT REQUEST DEFINITION AND SUFFIXES


"""


cp21 = {
    "i1": "Develop a musical piece named Viva using the given chord progression. 'Am', 'Bm', 'Em', 'Bm', 'C', 'D', 'G'",
    "i2": "Develop a musical piece named Viva using the given chord progression. 'Am', 'F#', 'Bm', 'Em', 'Am', 'F#', 'D', 'G'",
    "i2b": "Craft a musical works named Viva that follow the given chord alternations. 'Am', 'F#', 'Bm', 'Em', 'Am', 'F#', 'D', 'G'",
    "i2c": "Craft a musical works that follow the given chord. 'Am', 'Bm', 'Em', 'Bm', 'C'",
    "i3": "Craft a musical works named Viva that follow the given chord alternations. 'Am', 'F#', 'Bm', 'Em', 'Am', 'F#', 'D', 'G'",
    "i4": "Develop a basic chord alternation pattern that follow the given chord alternations 'Am', 'Bm', 'Em', 'Bm', 'C', 'D', 'G'",
    "i4b": "Develop a basic chord progression and resolution pattern that follow the given chord 'Am', 'Bm', 'Em', 'Bm', 'C', 'D', 'G'",
    "i4c": "Develop a basic chord progression and resolution pattern that follow the given chord 'Bm', 'Am', 'F#', 'Bm', 'Em'",
    "i4c2": "Develop a basic chord progression and resolution pattern that follow the given chord 'Bm', 'Am', 'F#', 'Bm', 'Em'",
    "i4c3": "Develop a basic chord progression and resolution pattern that follow the given chord 'Am' 'F#' 'Bm' 'Em'",
    "i5": "Develop a basic chord progression pattern that follow the given chord 'Am', 'Bm', 'Em', 'Bm', 'C', 'D', 'G'",
    "i6": "Develop a basic chord progression pattern that follow the given chord 'Am', 'F#', 'Bm', 'Em', 'Am', 'F#', 'D', 'G'",
    "i7": "Develop a basic chord progression and resolution pattern that follow the given chord 'Am', 'F#', 'Bm', 'Em', 'Am', 'F#', 'D', 'G'",
    "i8": "Develop a musical work based on 'Am', 'Bm', 'Em', 'Bm', 'C', 'D', 'G', 'Am', 'F#', 'Bm', 'Em', 'Am', 'F#', 'D', 'G'"
}


cp22= {
    "p1": "Develop a musical piece using the given chord progression. 'Am', 'Bm', 'Em', 'Bm', 'C', 'D', 'G'",
    "p2": "Develop a musical piece using the given chord progression. 'Am', 'F#dim', 'Bm', 'Em', 'Am', 'F#', 'D', 'G'",
    "p3": "Develop a musical piece using the given chord progression. 'Am', 'Bm', 'Em', 'Bm', 'C', 'D', 'G'",
    "p4": "Develop a musical piece using the given chord progression. 'Am', 'Bm', 'Em', 'Bm', 'C', 'D', 'G'",
    "p5": "Develop a musical piece using the given chord progression. 'Am', 'F#dim', 'Bm', 'Em', 'Am', 'F#dim', 'D', 'G'",
    "p6": "Develop a musical piece using the given chord progression. 'Am', 'Bm', 'Em', 'Bm', 'C', 'D', 'G'",
    "p7": "Develop a musical piece using the given chord progression. 'Am', 'Bm', 'Em', 'Bm', 'C', 'D', 'G'"
}


cp23= {
    "p1": "Develop a musical piece using the given chords. 'Am', 'Bm', 'Em', 'Bm', 'C', 'D', 'G'",
    "p2": "Develop a musical piece using the given chords. 'Am', 'F#dim', 'Bm', 'Em', 'Am', 'F#', 'D', 'G'",
    "p3": "Develop a musical piece using the given chords. 'Am', 'Bm', 'Em', 'Bm', 'C', 'D', 'G'",
    "p4": "Develop a musical piece using the given chords. 'Am', 'Bm', 'Em', 'Bm', 'C', 'D', 'G'",
    "p5": "Develop a musical piece using the given chords. 'Am', 'F#dim', 'Bm', 'Em', 'Am', 'F#dim', 'D', 'G'",
    "p6": "Develop a musical piece using the given chords. 'Am', 'Bm', 'Em', 'Bm', 'C', 'D', 'G'",
    "p7": "Develop a musical piece using the given chords. 'Am', 'Bm', 'Em', 'Bm', 'C', 'D', 'G'"
}


cp=cp23;cfx="23b"
cp=cp22;cfx="22b"
cp=cp21;cfx="21b"




output_json_of_choosen_pieces = f"{cname}_musical_pieces_{cfx}.json"
jcm.save_as_json_to_filename(cp,output_json_of_choosen_pieces)
for k,v in cp.items():
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
      output_filename = f"{cname}_{cfx}_{k}.json"
      jcm.save_as_json_to_filename(response,output_filename)
      time.sleep(1)
    except:
      print("k:",k,", v:",v, " Error: Could not save response as json")
      pass
  except:
    print("Error in inferences...")
    pass




#@STCIssue IN CASE
endpoint.pause()


endpoint:InferenceEndpoint=api.get_inference_endpoint(name=name,namespace=namespace,token=token)
print(endpoint)
