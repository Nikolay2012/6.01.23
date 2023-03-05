import os
import json

def find_path_to_file(name_file = ""):
    print("\n", __file__, "\n")
    path_to_file = __file__.split('/')
    # print("\n",path_to_file,"\n")
    del path_to_file[-1]
    # print("\n",path_to_file,"\n")
    del path_to_file[-1]
    # print("\n",path_to_file,"\n")
    path_to_file = '/'.join(path_to_file)
    # print("\n",path_to_file,"\n")
    path_to_file = os.path.join(path_to_file, name_file)
    return path_to_file

def load_json(file_to_path):
    with open(find_path_to_file(file_to_path), 'r') as file:
        dict1 = json.load(file)
        return dict1
# 
def dump_json(file_to_path, dict):
    with open(find_path_to_file(file_to_path), 'w') as file:
        json.dump(dict, file, ensure_ascii= False, indent=4)


