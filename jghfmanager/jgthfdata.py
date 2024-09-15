import yaml

import sys
import os

class JgHfConfig:
    def __init__(self, config_file):
        with open(config_file, 'r') as file:
            config_data = yaml.safe_load(file)
        
        self.huggingface = config_data['huggingface']
        #self.musical_pieces = config_data['musical_pieces']

