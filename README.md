# jghfmanager
HuggingFace EndPoint Manager - Ex. Boot a ChatMusician Endpoint, send some requests then suspend it.

1. Inferencer booting and executing the HuggingFace Endpoint described in the 'orpheus-config.yml'

```sh
pip install -U jghfmanager orpheuspypractice

#run 
cd mycreation_folder

ohfi
```


## Config

```yml
huggingface:
  name: chatmusician-myendpointname
  namespace: myusername
  repository: m-a-p/ChatMusician
  token_env_var: HUGGINGFACE_API_KEY
```

## Musical Inference request

```yml
musical:
  name: mycreationname
  sname: iterationname
  prompts:
    prompt1: "the prompt text...."
    prompt2: "another prompt or a variation...."
```

