import yaml

import sys
import os

class JgHfConfig:
    def __init__(self, config_file):
        with open(config_file, 'r') as file:
            config_data = yaml.safe_load(file)
        
        self.huggingface = config_data['huggingface']
        #self.musical_pieces = config_data['musical_pieces']

class JgHfMusicalPieces:
    def __init__(self, musical_pieces_file):
        with open(musical_pieces_file, 'r') as file:
            data = yaml.safe_load(file)

        self.musical = data['musical']

    def __str__(self) -> str:
        out_str=""
        piece=self.musical
        name=piece['name']
        sname=piece['sname']
        prompts=piece['prompts']
        out_str+=f"Musical Piece: {name}\n"
        out_str+=f"  Seq Name: {sname}\n"
        out_str+="  Prompts:\n"
        for k,v in prompts.items():
            out_str+=f"    {k}: {v}\n"
        return out_str