# jghfmanager
HuggingFace EndPoint Manager - Ex. Boot a ChatMusician Endpoint, send some requests then suspend it.

## Prototype

### 1. Inferencer booting and executing the HuggingFace Endpoint described in the 'orpheus-config.yml'

#### Install and run

```sh
pip install -U jghfmanager orpheuspypractice

#run 
cd mycreation_folder

ohfi
```


### Config

**orpheus-config.yml**

* in current folder or in your home folder

```yml
huggingface:
  name: chatmusician-myendpointname
  namespace: myusername
  repository: m-a-p/ChatMusician
  token_env_var: HUGGINGFACE_API_KEY
```

### Musical Inference request

**musical.yml**

* in current folder where is your creation.
* You can try a bot to help build your prompt (that you will need to convert into YAML): [Poe/jgwill/cmPengHelperAlpha](https://poe.com/cmPengHelperAlpha)

```yml
musical:
  name: mycreationname
  sname: iterationname
  prompts:
    prompt1: "the prompt text...."
    prompt2: "another prompt or a variation...."
```

