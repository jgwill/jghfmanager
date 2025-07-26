# CLAUDE.md - jghfmanager

## Project Overview

**jghfmanager** (>= 0.1.5) is a HuggingFace Endpoint Manager that provides automated management of HuggingFace inference endpoints. It specializes in booting ChatMusician endpoints, executing inference requests, and suspending resources to manage costs.

## Core Functionality

### CLI Tools
- **`ohfi`**: Main HuggingFace inference CLI (available when installed with orpheuspypractice)
- Automated endpoint lifecycle management (boot → inference → suspend)
- Configuration-driven endpoint setup

### Python Modules
- **`jghfmanager.cminferencer`**: Core inference engine
- **`jghfmanager.ensure_endpoint_paused`**: Endpoint state management
- **`jghfmanager.jgthfcli`**: CLI interface implementation
- **`jghfmanager.jgthfdata`**: Data handling and processing

## Configuration System

### orpheus-config.yml
Located in current directory or home folder:
```yaml
huggingface:
  name: chatmusician-myendpointname
  namespace: myusername
  repository: m-a-p/ChatMusician
  token_env_var: HUGGINGFACE_API_KEY
```

### musical.yml
Project-specific musical inference configuration:
```yaml
musical:
  name: mycreationname
  sname: iterationname
  prompts:
    prompt1: "the prompt text...."
    prompt2: "another prompt or a variation...."
```

## Usage Patterns

### Basic Workflow
```bash
# Install and setup
pip install -U jghfmanager orpheuspypractice

# Navigate to creation folder
cd mycreation_folder

# Run inference (boots endpoint, runs inference, suspends)
ohfi
```

### LangSmith Hub Integration
```python
from langchain import hub

tool_hub_tag = "jgwill/cmpenghelperbeta"
prompt_template = hub.pull(tool_hub_tag)
```

## Integration Context

This library serves as a critical component in the **orpheuspypractice** ecosystem:

- **Cost Management**: Automatically manages HuggingFace endpoint lifecycle to minimize compute costs
- **AI Music Generation**: Specialized for ChatMusician model interactions
- **Workflow Integration**: Works with jgcmlib for complete ABC notation generation pipeline
- **Configuration Driven**: Flexible endpoint management via YAML configuration

## Key Features

### Endpoint Management
- **Automated Boot**: Starts HuggingFace endpoints on demand
- **Inference Execution**: Handles model inference requests
- **Resource Cleanup**: Automatically suspends endpoints after use
- **Error Handling**: Robust error management for endpoint operations

### Music-Specific Features
- **ChatMusician Integration**: Optimized for music generation models
- **ABC Notation Support**: Generates ABC music notation via AI
- **Prompt Engineering**: Supports complex musical prompt templates
- **Batch Processing**: Can handle multiple musical prompts

## Development Notes

- **Version**: >= 0.1.5 (as required by orpheuspypractice)
- **Architecture**: Modular design with separate CLI and core functionality
- **Configuration**: YAML-based configuration system
- **Dependencies**: HuggingFace API, LangChain Hub integration
- **Build System**: Standard Python setuptools with Makefile

## External Integrations

### HuggingFace
- **Endpoint API**: Direct integration with HuggingFace inference endpoints
- **Model Repository**: Supports m-a-p/ChatMusician and other music models
- **Authentication**: Token-based authentication via environment variables

### LangChain Ecosystem  
- **Hub Integration**: Connects to LangSmith Hub for prompt templates
- **Tool Support**: Compatible with LangChain tooling ecosystem
- **Prompt Engineering**: Advanced prompt template management

## Important Context

This manager bridges AI model infrastructure with music generation workflows:

1. **Cost-Conscious Design**: Primary focus on managing expensive GPU resources efficiently
2. **Music Generation Specialized**: Optimized for ChatMusician and similar music AI models
3. **Configuration-First**: Behavior driven by YAML configuration files
4. **Integration Ready**: Designed to work seamlessly with orpheuspypractice workflows

The manager enables cost-effective AI music generation by automating the complex lifecycle of cloud-based inference endpoints.